#!/bin/env python2

# This file is part of OpenQUA.
# 
# Copyright (c) 2014 Derecho and contributors. All rights reserved.
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

import urllib2, time
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from pyhamtools.locator import locator_to_latlong, latlong_to_locator

from repeater import Repeater

veron_data = urllib2.urlopen("http://www.veron.nl/naslag/naslag_repeaters.html").read()
veron_soup = BeautifulSoup(veron_data)

geolocator = Nominatim()

# We're skipping the last block as it lists external resources and isn't
# actually a table with repeater information.
repeater_category_titles = [
            repeater_category_title.next_element.strip()
            for repeater_category_title
            in veron_soup.find_all(class_="tekstbloktitel")
        ][:-1]

i = 0
previous_repeater_info = None
for repeater_category in veron_soup.find_all(class_="tekstblok")[:-1]:
    for row in repeater_category.find_all("tr"):
        if row.find("th"):
            continue

        repeater_info = [
                    cell.next_element.strip()
                    for cell
                    in row.find_all("td")
                ]
        repeater_category_title = repeater_category_titles[i]

        # Some entries reuse values from the previous row
        if len(repeater_info) == 3:
            fixed_repeater_info = [repeater_info[0]]
            fixed_repeater_info += [previous_repeater_info[1]]
            fixed_repeater_info += [repeater_info[1]]
            fixed_repeater_info += [repeater_info[2]]
            fixed_repeater_info += [previous_repeater_info[4]]
            fixed_repeater_info += [previous_repeater_info[5]]
            repeater_info = fixed_repeater_info
        elif len(repeater_info) != 6:
            # Shouldn't happen, but better not crash.
            continue

        repeater = Repeater(repeater_info[0])
        repeater.tx = float(repeater_info[3].replace(',', '.'))
        repeater.rx = float(repeater_info[2].replace(',', '.'))
        if "FM" in repeater_category_title:
            if repeater_info[5] != '-':
                repeater.to = float(repeater_info[5].replace(',', '.'))
            repeater.mo = "FM"
        elif "D-Star" in repeater_category_title:
            repeater.mo = "D-Star"
        elif "Packetradio" in repeater_category_title:
            repeater.mo = "Packetradio"
            # TODO Add baudrate from repeater_info[5]
        repeater.ml = repeater_info[4]
        repeater.lo = repeater_info[1]
        if repeater.ml == "?":
            location = geolocator.geocode(repeater.lo + " Netherlands", timeout=10)
            repeater.lat = location.latitude
            repeater.lon = location.longitude
            repeater.ml = latlong_to_locator(repeater.lat, repeater.lon)
            time.sleep(2)
        else:
            repeater.lat, repeater.lon = locator_to_latlong(repeater.ml)

        print(repeater)
        repeater.insert()
        previous_repeater_info = repeater_info
    i += 1
