import requests

def get_aprs_data(callsign):
    callsigns = ",".join([callsign + "-" + ssid for ssid in "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
    callsigns = callsign + "," + callsigns
    url = "http://api.aprs.fi/api/get?name={0}&what=loc&apikey=67665.2kj3rm2Krg8PplOA&format=json".format(callsigns)
    result = requests.get(url)
    if result.status_code != 200:
        raise ValueError("APRS API status code != 200")
    return result.json()
