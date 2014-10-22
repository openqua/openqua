
import mysql.connector

class Database:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='openqua',
                                      password='xxxxxxxxx',
                                      host='127.0.0.1', database='openqua')

    def get_repeater(self, callsign):
        cursor = self.cnx.cursor()
        query = "SELECT * FROM repeater WHERE callsign = %s"
        repeater = None
        cursor.execute(query, (callsign,))
        for (callsign, rx, tx, to, mo, ml, lo, ke, lat, lon) in cursor:
            repeater =  { 'callsign': callsign,
                     'rx': rx,
                     'tx': tx,
                     'to': to,
                     'mo': mo,
                     'ml': ml,
                     'lo': lo,
                     'ke': ke,
                     'lat': lat,
                     'lon': lon }
        cursor.close()
        return repeater

    def get_all_repeaters(self):
        cursor = self.cnx.cursor()
        query = "SELECT station.callsign, rx, tx, ctcss, mode, locator, town, keeper, lat, lon FROM station, station_repeater WHERE station.callsign = station_repeater.callsign"
        cursor.execute(query)
        repeaters = []
        for (callsign, rx, tx, to, mo, ml, lo, ke, lat, lon) in cursor:
            repeater =  { 'callsign': callsign,
                     'rx': rx,
                     'tx': tx,
                     'to': to,
                     'mo': mo,
                     'ml': ml,
                     'lo': lo,
                     'ke': ke,
                     'lat': lat,
                     'lon': lon }
            repeaters.append(repeater)
        return repeaters


    def close(self):
        self.cnx.close()


