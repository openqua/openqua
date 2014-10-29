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

# While DARC offers repeater data for many countries, this script only scrapes
# the german ones. This is because DARC is the official authority that handles
# their registration. All info from other counties has been collected by them
# elsewhere.

import urllib2
import csv
from pyhamtools.locator import locator_to_latlong

from repeater import Repeater

def get_repeater_data(locator):
    """Fetches CSV data for up to 600 repeaters nearest to the given locator"""
    darc_data = urllib2.urlopen("http://echorelais.darc.de/cgi-bin/relais.pl?lat_deg=50&lat_min=58.75&lat_NS=Nord&lon_deg=10&lon_min=02.50&lon_EW=Ost&city=&sel=gridsq&gs={}&ctrcall=&dxcc=DL&maxgateways=600&printas=csv&type=DL3EL&type=el&type=il&type=ds&type=dm&type=Baken&kmmls=km".format(locator)).read()
    # Get rid of headings and instruction footer
    darc_lines = darc_data.split('\n')[1:-2]

    # Get rid of distance to locator
    return_data = ""
    for line in darc_lines:
        return_data += ';'.join(line.split(';')[:-1]) + '\n'

    return return_data

def assemble_repeater_data(locators):
    """Fetches CSV data for each locator and returns the unique assembled repeater list as CSV data"""
    unique_repeaters = set()

    for locator in locators:
        repeater_data = get_repeater_data(locator)
        for line in repeater_data.split('\n'):
            unique_repeaters.add(line)

    return '\n'.join(unique_repeaters)

# Assuming these four locations will result in a complete set
data = assemble_repeater_data(["JO41AD", "JO53BJ", "JO62FD", "JN59EH"])

# Clean it up a bit
data = data.replace('\r', '')
data = data.replace('&deg;', ' ')

for row in csv.reader(data.split('\n'), delimiter=';'):
    if len(row) != 9:
        continue
    repeater = Repeater(row[0])
    try:
        repeater.tx = float(row[1].replace(',', '.'))
    except ValueError:
        # Some data is just wrong or malformatted
        pass
    if (row[2] != '') and (row[2] != 'Beacon'):
        try:
            repeater.rx = float(row[2].replace(',', '.'))
        except ValueError:
            pass
    if row[8] == 'DMR':  # Unfortunately, most will be missing this
        repeater.mode = row[8]
    if row[7] != '':
        repeater.ctcss = float(row[7].replace(',', '.'))
        repeater.mode = "FM"
    repeater.locator = row[3]
    # The fourth column is actually info, and *usually* has the town name.
    # It may be something different, or have additional information.
    # TODO Get town name based on lat/long or locator
    repeater.town = ' '.join(row[4].split())  # Remove consecutive whitespace
    repeater.lat, repeater.lon = locator_to_latlong(repeater.locator)
    repeater.source = "http://echorelais.darc.de/"
    print(repeater)
    repeater.update()
