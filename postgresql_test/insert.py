#!/usr/bin/python2
import json 
import psycopg2
from datetime import datetime

try:
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "test", host = "127.0.0.1", port = "5432")
    print "Opened database successfully"
except psycopg2.Error as e:
    print e

with open('PATH_PATH') as jsdata:
    data = json.load(jsdata)
    for mac in data:
        try:
            mac_inf = mac['mac']
            tim_e = int(str(datetime.now().time())[0:2])
            cur = conn.cursor()
            query = "insert into polaczenia (mac_adr, godzina) VALUES (%s, %s);"
            data = (mac_inf, tim_e)
            cur.execute(query, data)
            conn.commit()
            print "Add ", mac_inf
        except psycopg2.Error as e:
            print(e)
            print "Cannot insert into polaczenia"
