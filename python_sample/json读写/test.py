#coding:utf-8
'''
import rpyc

import os
r = open("log_all.txt","r")
print r.read()
'''


'''
import MySQLdb
conn=MySQLdb.connect(host="192.168.40.195",user="root",passwd="163a163@",db="mhcalendar",charset="utf8")    
cursor = conn.cursor()
n = cursor.execute("select * from session") 
print n     
for row in cursor.fetchall():      
    print row  
    print row[1].encode('utf-8')


test = 3 
print test >> 2
for i in range(10):
	if (i>>2) % 2 != 0:
		print i
'''


import json
test = (23,'3',33)
alldata = []
alldata.append(test)
test = (12,'23',23)
alldata.append(test)
print alldata
json.dump(alldata, open('newjsonfile.dat', 'w'))
fuckdata = json.load(open('newjsonfile.dat', 'r'))
print fuckdata
for i in fuckdata[0]:
	print i


print 