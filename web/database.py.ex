
import mysql.connector

class Database:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='openqua',
                                      password='xxxxxxxx',
                                      host='127.0.0.1', database='openqua')

    def get_repeater(self, callsign):
        cursor = self.cnx.cursor()
        query = "SELECT station.callsign, ssid, rx, tx, carrier, burst, ctcss, dcs, mode, locator, town, keeper, lat, lon, station_repeater.lastupdated, station_repeater.source FROM station, station_repeater WHERE station.callsign = station_repeater.callsign AND station.callsign = %s"
        cursor.execute(query, (callsign,))
        ssids = []
        for (callsign, ssid, rx, tx, carrier, burst, ctcss, dcs, mode, locator, town, keeper, lat, lon, lastupdated, source) in cursor:
            repeater =  { 'callsign': callsign + ("-" + ssid if ssid != "1" else ""),
                     'rx': float(rx),
                     'tx': float(tx),
                     'carrier': carrier,
                     'burst': burst,
                     'ctcss': float(ctcss),
                     'dcs': float(dcs),
                     'mode': mode,
                     'locator': locator,
                     'town': town,
                     'keeper': keeper,
                     'lat': float(lat),
                     'lon': float(lon),
                     'lastupdated': lastupdated,
                     'source': source }
            ssids.append(repeater)
        return ssids

    def get_all_repeaters(self):
        cursor = self.cnx.cursor()
        query = "SELECT station.callsign, ssid, rx, tx, carrier, burst, ctcss, dcs, mode, locator, town, keeper, lat, lon, station_repeater.lastupdated, station_repeater.source FROM station, station_repeater WHERE station.callsign = station_repeater.callsign"
        cursor.execute(query)
        repeaters = []
        for (callsign, ssid, rx, tx, carrier, burst, ctcss, dcs, mode, locator, town, keeper, lat, lon, lastupdated, source) in cursor:
            repeater =  { 'callsign': callsign + ("-" + ssid if ssid != "1" else ""),
                     'rx': float(rx),
                     'tx': float(tx),
                     'carrier': carrier,
                     'burst': burst,
                     'ctcss': float(ctcss),
                     'dcs': float(dcs),
                     'mode': mode,
                     'locator': locator,
                     'town': town,
                     'keeper': keeper,
                     'lat': float(lat),
                     'lon': float(lon),
                     'lastupdated': lastupdated,
                     'source': source }
            repeaters.append(repeater)
        return repeaters

    def get_club(self, callsign):
        cursor = self.cnx.cursor()
        query = "SELECT station.callsign, keeper, name, locator, town, lat, lon, station_club.lastupdated, station_club.source FROM station, station_club WHERE station.callsign = station_club.callsign AND station.callsign = %s"
        cursor.execute(query, (callsign,))
        club = None
        for (callsign, keeper, name, locator, town, lat, lon, lastupdated, source) in cursor:
            club =  { 'callsign': callsign,
                     'name': name,
                     'locator': locator,
                     'town': town,
                     'lat': float(lat),
                     'lon': float(lon),
                     'contact': keeper,
                     'lastupdated': lastupdated,
                     'source': source }
        return club


    def get_all_clubs(self):
        cursor = self.cnx.cursor()
        query = "SELECT station.callsign, keeper, name, locator, town, lat, lon, station_club.lastupdated, station_club.source FROM station, station_club WHERE station.callsign = station_club.callsign"
        cursor.execute(query)
        clubs = []
        for (callsign, keeper, name, locator, town, lat, lon, lastupdated, source) in cursor:
            club =  { 'callsign': callsign,
                     'name': name,
                     'locator': locator,
                     'town': town,
                     'lat': float(lat),
                     'lon': float(lon),
                     'contact': keeper,
                     'lastupdated': lastupdated,
                     'source': source }
            clubs.append(club)
        return clubs

    def close(self):
        self.cnx.close()

