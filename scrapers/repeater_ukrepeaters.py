
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

from urllib2 import urlopen
import csv

from repeater import Repeater

CSV_URL = "http://www.ukrepeater.net/csvcreate.php"

# Format of CSV file is:
#
# * Callsign
# * Band
# * Channel
# * TX Frequency
# * RX Frequency
# * Mode
# * Maidenhead Locator
# * Natural Language Location
# * National Grid Reference
# * Region
# * CTCSS Tone
# * Keeper Callsign
# * Latitude
# * Longitude
#
# The first line of the file is a header and should be discarded.
# The fields are seperated by commas and quoted with double quotes.

f = urlopen(CSV_URL)

data = csv.reader(f, delimiter=',', quotechar='"')
for row in data:
    repeater = Repeater(row[0])
    repeater.tx = row[3]
    repeater.rx = row[4]
    repeater.to = row[10]
    repeater.mo = row[5]
    repeater.ml = row[6]
    repeater.lo = row[7]
    repeater.ke = row[11]
    repeater.lat = row[12]
    repeater.lon = row[13]
    repeater.prnt()
    repeater.insert()

f.close()

