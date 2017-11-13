#!/usr/bin/python2

import psycopg2

from datetime import datetime

try:
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "test", host = "127.0.0.1", port = "5432")
    print "Opened database successfully"
except psycopg2.Error as e:
    print e
try:
    quer = "SELECT godzina, COUNT(*) FROM polaczenia GROUP BY godzina ORDER BY godzina;"
    cur = conn.cursor()
    cur.execute(quer)
	
	if(cur.rowcount == 0):	# CHECK IF WORK
		print "No data!!!"
	else:	
		rows = cur.fetchall()
		#tab = [str(rows[0])[15:17]]
		#del rows[0]
		#print tab
		for row in rows:
			print row
			#print(str(row)[15:17])

except psycopg2.Error as e:
    print(e)
    print "SELECT error"