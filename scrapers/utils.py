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

def freq_to_band(freq):
    """Convert given frequency in Mhz to a bandname (all regions)"""
    if freq >= 0.1357 and freq <= 0.1378:
        return "2200m"
    elif freq >= 0.472 and freq <= 0.479:
        return "600m"
    elif freq >= 1.8 and freq <= 2.0:
        return "160m"
    elif freq >= 3.5 and freq <= 4.0:
        return "80m"
    elif freq >= 5.25 and freq <= 5.45:
        return "60m"
    elif freq >= 7.0 and freq <= 7.3:
        return "40m"
    elif freq >= 10.1 and freq <= 10.15:
        return "30m"
    elif freq >= 14.0 and freq <= 14.35:
        return "20m"
    elif freq >= 18.068 and freq <= 18.168:
        return "17m"
    elif freq >= 21.0 and freq <= 21.45:
        return "15m"
    elif freq >= 24.89 and freq <= 24.99:
        return "12m"
    elif freq >= 28.0 and freq <= 29.7:
        return "10m"
    elif freq >= 50.0 and freq <= 54.0:
        return "6m"
    elif freq >= 70.0 and freq <= 70.5:
        return "4m"
    elif freq >= 144.0 and freq <= 148.0:
        return "2m"
    elif freq >= 222.0 and freq <= 225.0:
        return "1.25m"
    elif freq >= 420.0 and freq <= 450.0:
        return "70cm"
    elif freq >= 902.0 and freq <= 928.0:
        return "33cm"
    elif freq >= 1240.0 and freq <= 1300.0:
        return "23cm"
    elif freq >= 2300.0 and freq <= 2450.0:
        return "13cm"
    elif freq >= 3300.0 and freq <= 3500.0:
        return "9cm"
    elif freq >= 5650.0 and freq <= 5925.0:
        return "5cm"
    elif freq >= 10000.0 and freq <= 10500.0:
        return "3cm"
    elif freq >= 24000.0 and freq <= 24250.0:
        return "1.2cm"
    elif freq >= 47000.0 and freq <= 47200.0:
        return "6mm"
    elif freq >= 75500.0 and freq <= 81500.0:
        return "4mm"
    elif freq >= 122250.0 and freq <= 123000.0:
        return "2.5mm"
    elif freq >= 134000.0 and freq <= 141000.0:
        return "2mm"
    elif freq >= 241000.0 and freq <= 250000.0:
        return "1mm"
    else:
        return "unknown"
