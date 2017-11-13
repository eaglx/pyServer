#!/usr/bin/python2

import psycopg2

from datetime import datetime

try:
													# database name, user, password, host ip, port
	conn = psycopg2.connect(database="postgres", user = "postgres", password = "test", host = "127.0.0.1", port = "5432")
    print "Opened database successfully"

    quer = "SELECT godzina, COUNT(DISTINCT adr_mac) FROM polaczenia GROUP BY godzina ORDER BY godzina;"
    cur = conn.cursor()
    cur.execute(quer)
    
	listVal = []
	listCount = []
	
	if(cur.rowcount == 0):	# CHECK IF WORK
		print "No data!!!"
	else:	
		rows = cur.fetchall()
		for row in rows:
			tab.append[row]
			
		countVal = 1
		oldVal = tab[0]
		listVal = [oldVal]
		listCount = []
		del tab[0]
		for ele in tab:
			if ele != oldVal:
				listVal.append(ele)
				listCount.append(countVal)
				countVal = 1
				oldVal = ele        
			else:
				countVal += 1
		listCount.append(countVal)
		print(listVal)
		print(listCount)
                
    plt.bar(listVal, listCount)

    #plt.set_ticks(listVal)                #wyskalowanie osi X aby wartosci na dolnej i gornej osi byly zgodne
    #.set_xticklabels(["0", "40", "80", "120", "160", "200"])
    plt.xlabel('time (h)')
    plt.ylabel('number of devices')
    plt.title('Plot')
    plt.grid(True)
    plt.savefig("chart.png")
    
except psycopg2.Error as e:
    print e
