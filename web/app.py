
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
import re, subprocess
from flask import Flask, jsonify
app = Flask(__name__)
db = Database()

@app.route("/")
def hello():
    return "OpenQUA!"

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
    repeater = db.get_repeater(callsign.upper())
    if repeater == None:
        return detail
    detail['repeater'] = {
            'tx': repeater['tx'],
            'rx': repeater['rx'],
            'tone': repeater['to'],
            'mode': repeater['mo'],
            'keeper': repeater['ke']
            }
    detail['lat'] = repeater['lat']
    detail['lon'] = repeater['lon']
    detail['locator'] = repeater['ml']
    detail['town'] = repeater['lo']
    return detail

@app.route("/j/<callsign>")
def callsign_detail_json(callsign):
    detail = get_dxcc(callsign)
    detail = add_repeater_detail(callsign, detail)
    # TODO Get beacon data from database
    # TODO Get APRS-IS data from APRS-IS
    # TODO Get Echolink data from database
    return jsonify(detail)

if __name__ == "__main__":
    app.run(debug=True)

