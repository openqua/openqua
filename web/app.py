
# This file is part of OpenQUA.
# 
# Copyright (c) 2014 Iain R. Learmonth and contributors. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# * Neither the name of openqua nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from database import Database
import re, subprocess, aprs, wsprnet
from flask import Flask, jsonify, render_template, redirect, request
app = Flask(__name__)


def get_dxcc(callsign):
    callsign = callsign.upper()
    detail = {'callsign': callsign}
    callsign = re.sub("[^A-Z0-9]", "", callsign)
    p = subprocess.Popen(['dxcc', callsign], stdout=subprocess.PIPE)
    out, err = p.communicate()
    lines = out.split("\n")
    detail['dxcc'] = re.sub("^Country Name:", "", lines[3]).strip()
    detail['waz'] = re.sub("^WAZ Zone:", "", lines[4]).strip()
    detail['itu'] = re.sub("^ITU Zone:", "", lines[5]).strip()
    detail['continent'] = re.sub("^Continent:", "", lines[6]).strip()
    detail['lat'] = re.sub("^Latitude:", "", lines[7]).strip()
    detail['lon'] = re.sub("^Longitude:", "", lines[8]).strip()
    detail['utcshift'] = re.sub("^UTC shift:", "", lines[9]).strip()
    return detail

def add_repeater_detail(callsign, detail):
    db = Database()
    repeater = db.get_repeater(callsign.upper())
    if len(repeater) == 0:
        return detail
    print repeater
    detail['repeater'] = repeater
    detail['lat'] = float(repeater[0]['lat'])
    detail['lon'] = float(repeater[0]['lon'])
    detail['locator'] = repeater[0]['locator']
    detail['town'] = repeater[0]['town']
    return detail

def add_club_detail(callsign, detail):
    db = Database()
    club = db.get_club(callsign.upper())
    if club == None:
        return detail
    detail['club'] = club
    detail['lat'] = float(club['lat'])
    detail['lon'] = float(club['lon'])
    detail['locator'] = club['locator']
    detail['town'] = club['town']
    detail['keeper'] = club['keeper']
    return detail

def get_callsign_detail(callsign):
    detail = get_dxcc(callsign)
    detail = add_repeater_detail(callsign, detail)
    detail = add_club_detail(callsign, detail)
    # TODO Get beacon data from database
    # TODO Get APRS-IS data from APRS-IS
    # TODO Get Echolink data from database
    return detail

@app.route("/api/0.1/repeaters.json")
def api_repeaters_json():
    db = Database()
    return jsonify({'repeaters': db.get_all_repeaters()})

@app.route("/api/0.1/repeater/<callsign>.json")
def api_repeater_json(callsign):
    db = Database()
    return jsonify({'repeater': db.get_repeater(callsign.upper())})

@app.route("/api/0.1/clubs.json")
def api_clubs_json():
    db = Database()
    return jsonify({'clubs': db.get_all_clubs()})

@app.route("/api/0.1/club/<callsign>.json")
def api_club_json(callsign):
    db = Database()
    return jsonify({'club': db.get_club(callsign.upper())})

@app.route("/api/0.1/callsign/<callsign>.json")
def callsign_detail_json(callsign):
    detail = get_callsign_detail(callsign)
    return jsonify(detail)

@app.route("/map")
def repeaters_map():
    db = Database()
    return render_template("map.html", repeaters = db.get_all_repeaters(), clubs=db.get_all_clubs())

@app.route("/api/")
def redirect_latest_api():
    return redirect("/api/0.1/")

@app.route("/api/0.1/")
def api_0_1_docs():
    return render_template("api_0_1.html")

@app.route("/c/")
def callsign_no_callsign():
    return redirect("/")

@app.route("/c/<callsign>")
def callsign_detail_page(callsign):
    detail = get_callsign_detail(callsign)
    return render_template("callsign.html", callsign = detail, aprs = aprs.get_aprs_data(callsign), wspr = wsprnet.get_wspr_data(callsign))

@app.route("/search")
def callsign_search():
    callsign = request.args.get("callsign")
    return redirect("/c/" + callsign)

@app.route("/")
def hello():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

