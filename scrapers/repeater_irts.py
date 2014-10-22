#!/bin/env python2

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

import urllib2, time, re
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from pyhamtools.locator import locator_to_latlong, latlong_to_locator
from geopy.geocoders import Nominatim

from repeater import Repeater

irts_data = urllib2.urlopen("http://www.irts.ie/cgi/repeater.cgi?printable").read()
irts_soup = BeautifulSoup(irts_data)

geolocator = Nominatim()

repeater_rows = irts_soup.find_all('table')[0].find_all('tr')

count = 0

for row in repeater_rows:
    count = count + 1
    if count == 1:
        continue # Skip the header row
    fields = row.find_all('td')
    repeater = Repeater(fields[2].next_element.strip())
    if repeater.callsign[0:2] == "GB":
        continue # we get these anyway from ukrepeater
    repeater.rx = fields[1].next_element.next_element.next_element.strip()
    repeater.tx = fields[1].next_element.next_element.next_element.next_element.next_element.next_element.next_element.strip()
    activation = re.sub("\/", "", fields[3].next_element.strip())
    if activation == "Carrier":
        repeater.carrier = True
    elif activation == "1750Hz":
        repeater.burst = True
    else:
        repeater.ctcss = re.sub("Hz", "", activation)
    repeater.mode = "FM"
    repeater.town = fields[4].next_element.strip()
    location = geolocator.geocode(re.sub(",.*$", "", repeater.town) + ", Republic of Ireland", timeout=10)
    if location == None:
        continue # TODO need to get a better geocoding system, or actually pull out the ml
    repeater.lat = location.latitude                                     
    repeater.lon = location.longitude                                    
    repeater.locator = latlong_to_locator(repeater.lat, repeater.lon)
    time.sleep(2)
    repeater.source = "http://www.irts.ie/"
    print repeater
    repeater.update()

