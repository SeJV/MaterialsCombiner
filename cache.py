import sqlite3
from datetime import datetime
from dateutil import parser

class Cache:
    def __init__(self, file, expired_in_seconds):
        self._expired = expired_in_seconds
        self._conn = sqlite3.connect(file)
        self._cursor = self._conn.cursor()
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS requests
                            (request text, response text, expired text)''')
        self._conn.commit()

    def getResponse(self, request):
        t = (request,)
        self._cursor.execute('SELECT * FROM requests WHERE request=?', t)
        data = self._cursor.fetchone()

        if not data:
            return None

        delta = datetime.now() - parser.parse(data[2])

        if delta.seconds > self._expired:
            return None

        return data[1]

    def saveResponse(self, request, response):
        t = (request, response, datetime.now())
        self._cursor.execute('INSERT INTO requests VALUES (?,?,?)', t)
        self._conn.commit()

    def close(self):
        self._conn.close()

