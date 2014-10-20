
import mysql.connector

class Database:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='openqua',
                                      password='xxxxxxxxxxxxxx',
                                      host='127.0.0.1', database='openqua')

    def insert(self, query, data):
        cursor = cnx.cursor()
        cursor.execute(query, data)
        cnx.commit()
        cursor.close()

    def close(self):
        self.cnx.close()


