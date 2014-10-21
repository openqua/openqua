
import mysql.connector

class Database:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root',
                                      password='secret',
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

    def close(self):
        self.cnx.close()


