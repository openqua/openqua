
from urllib2 import urlopen

CSV_URL = "http://www.ukrepeater.net/csvcreate.php"

f = urlopen(CSV_URL)
csv = f.readlines()
f.close

print csv


