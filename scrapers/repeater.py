
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

class Repeater:

    def __init__(self, callsign):
        ident = callsign.split('-')
        if len(ident) == 1:
            self.callsign = callsign
            self.ssid = 1
        else:
            self.callsign = ident[0]
            self.ssid = ident[1]
        self.keeper = None
        self.mode = "FMVOICE"
        self.tx = 0
        self.rx = 0
        self.carrier = False
        self.burst = False
        self.ctcss = 0
        self.dcs = 0
        self.town = ""
        self.ml = ""
        self.source = "http://www.example.com/"

    def __str__(self):
        return "----------\n" + \
        "Callsign: {}\n".format(self.callsign,) + \
        "Repeater Keeper: {}\n".format(self.keeper,) + \
        "SSID: {}\n".format(self.ssid,) + \
        "Mode: {}\n".format(self.mode,) + \
        "TX Frequency: {}\n".format(self.tx,) + \
        "RX Frequency: {}\n".format(self.rx,) + \
        "Carrier Activation: {}\n".format(self.carrier,) + \
        "1750Hz Burst Tone Activation: {}\n".format(self.burst,) + \
        "CTCSS Tone: {}\n".format(self.ctcss,) + \
        "DCS Tone: {}\n".format(self.dcs,) + \
        "Town: {}\n".format(self.town,) + \
        "Maidenhead Locator: {}\n".format(self.locator,) + \
        "Latitude: {}    Longitude: {}\n".format(self.lat, self.lon) + \
        "Source: {}\n".format(self.source,) + \
        "----------"

    def update(self):
        db = Database()
        query = "REPLACE INTO station " \
                "VALUES ( %s, NULL, %s, NULL, %s );"
        data = (self.callsign, self.keeper, self.source)
        db.insert(query, data)
        query = "REPLACE INTO station_repeater " \
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NULL, %s );"
        data = (self.callsign, self.ssid, self.mode, self.tx, self.rx, self.carrier, self.burst, self.ctcss, self.dcs, self.town, self.locator, self.lat, self.lon, self.source)
        db.insert(query, data)
        db.close()

