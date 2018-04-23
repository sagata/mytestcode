#coding:utf-8
from pymongo import MongoClient
c = {
	'user':'root',
	'password':'root123',
	'ip':'192.168.40.195',
	'port':27017,
}
uri = "mongodb://%s:%s@%s:%s"%(c['user'],c['password'],c['ip'],c['port'])
conn = MongoClient(uri)
db = conn.mhcalendar
collection = db.test
data = collection.find({'test':'test3'})
thisdata = data[0]['data']
hehe =  list(set(thisdata + ['test11']))
print type(hehe)
print hehe
#data = collection.insert({'test':'test3','data':['test11']})
#print str(data)
#print data['test']
'''
# 添加单条数据到集合中 
user = {"name":"cui","age":"10"} 
collection = db.test 
collection.insert(user) 
''' 
'''
#同时添加多条数据到集合中  
users=[{"name":"cui","age":"9"},{"name":"cui","age":"11"}]  
collection.insert(users)  
'''

'''
#简单参数查询  
for data in collection.find({"name":"1"}):  
    print data  
'''


'''
db = conn.mhcalendar
	collection = db.session
	collection.insert(readyinsertdata) 
	'''

