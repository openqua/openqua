
import requests
from bs4 import BeautifulSoup

WSPRNET_DB_URL = "http://wsprnet.org/drupal/wsprnet/spotquery"

def get_wspr_data(callsign):

    query = {
            'band': 'All',
            'count': '10',
            'call': callsign,
            'reporter': '',
            'timelimit': '1209600',
            'sortby': 'date',
            'unique': '1',
            'sortrev': '1',
            'op': 'update',
            'form_id': 'wsprnet_spotquery_form'
            }

    r = requests.post(WSPRNET_DB_URL, data=query)

    soup = BeautifulSoup(r.text)
    spots = []

    count = 0

    for row in soup.find_all('tr'):
        count += 1
        if count == 1:
            continue # Skip the header
        fields = row.find_all('td')
        spot = {
                'timestamp': fields[0].next_element.strip(),
                'srccall': fields[1].next_element.strip(),
                'freq': fields[2].next_element.strip(),
                'snr': fields[3].next_element.strip(),
                'drift': fields[4].next_element.strip(),
                'grid': fields[5].next_element.strip(),
                'pwr': fields[6].next_element.strip(),
                'rptcall': fields[7].next_element.strip(),
                'rptgrid': fields[8].next_element.strip(),
                'distance': fields[9].next_element.strip(),
                'az': fields[10].next_element.strip(),
                }
        spots.append(spot)

    return spots

