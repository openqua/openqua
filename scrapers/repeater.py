
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
        self.callsign = callsign
        self.tx = 0.0
        self.rx = 0.0
        self.to = 0.0
        self.mo = ''
        self.ml = ''
        self.lo = ''
        self.ke = ''
        self.lat = ''
        self.lon = ''

    def __str__(self):
        return "----------\n" + \
        "Callsign: {}\n".format(self.callsign,) + \
        "TX Frequency: {}\n".format(self.tx,) + \
        "RX Frequency: {}\n".format(self.rx,) + \
        "CTCSS Tone: {}\n".format(self.to,) + \
        "Mode: {}\n".format(self.mo,) + \
        "Maidenhead Locator: {}\n".format(self.ml,) + \
        "Natural Language Location: {}\n".format(self.lo,) + \
        "Repeater Keeper: {}\n".format(self.ke,) + \
        "Latitude: {}    Longitude: {}\n".format(self.lat, self.lon) + \
        "----------"

    def mysql(self):
        query = "REPLACE INTO repeater " \
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s );"
        data = (self.callsign, self.tx, self.rx, self.to, self.mo, self.ml, self.lo, self.ke, self.lat, self.lon)
        return (query, data)

    def insert(self):
        db = Database()
        query, data = self.mysql()
        db.insert(query, data)
        db.close()


