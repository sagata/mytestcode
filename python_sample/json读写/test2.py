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
test = {'first':'xiaoyang','second':'sabi'}
test2 = {'first':'hehe','second':'da'}
alldata = []
alldata.append(test)
alldata.append(test2)

print alldata
json.dump(alldata, open('newjsonfile.dat', 'w'))
fuckdata = json.load(open('newjsonfile.dat', 'r'))
print fuckdata
for i in fuckdata[0]:
	print i


temp = 'xyn3037|sdfa'
temp2 = ['xyn3037','fdaf']
print '|'.join(temp2)

test11 = 'abcbc'
print test11.find('11bc')

test2 = "[u'test1',u'test2']"
a = '{"isOK": 1, "isRunning": 1, "isError": 1}'
print json.loads(a)
print test2.replace("u'","")

test = 'test'
print test.find('')

dicttest = {'1':'test','2':'tes2'}
dicttest.pop('1')
print dicttest

cal = 102/100*112750*(40/100 + 5*12/100)*(78/100 + 10*4/100) + 0
cal2 = float(40)/float(100) + 5*12/100
print cal2

test = ['111','222','3333']
print test[-1]