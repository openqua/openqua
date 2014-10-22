
import urllib2, time, re
from xml.dom.minidom import parse
from pyhamtools.locator import latlong_to_locator
from geopy.geocoders import Nominatim

from club import Club

rsgb_url = "http://www.rsgbdata.net/clubinfo/process.php?lat=55&lng=0&radius=900"
rsgb_handle = urllib2.urlopen(rsgb_url)
rsgb_xml = parse(rsgb_handle)
rsgb_handle.close()

geolocator = Nominatim()
prog = re.compile("[2GM][A-Z]?[0-9][A-Z]+")

for row in rsgb_xml.getElementsByTagName("marker"):
    c = Club(row.attributes['clubcall'].value)
    if c.callsign.startswith("RS"):
        continue # not a real callsign
    c.town = c.name = row.attributes['clubname'].value
    c.lat = row.attributes['lat'].value
    c.lon = row.attributes['lng'].value
    c.locator = latlong_to_locator(float(c.lat), float(c.lon))
    address = geolocator.reverse((float(c.lat), float(c.lon))).address.split(", ")
    if len(address) < 4:
        c.town = address[1]
    else:
        c.town = address[2]
    contact = row.attributes['contact'].value
    keepers = prog.findall(contact)
    if len(keepers) != 0:
        c.keeper = keepers[0]
    c.source = "http://rsgb.org/"
    print c
    c.update()
    time.sleep(5)

