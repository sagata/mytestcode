# -*- coding:utf-8 -*-
import urllib2
import urllib
import json
from time import localtime,strftime
def getmap():
	user_map = {}
	convert_usermap = {}
	alluser = user.select()
	for each in alluser:
		user_map[each.username] = each.realname
		convert_usermap[each.realname] = each.username
	return user_map,convert_usermap

def send_msg(name,msg):
	#name = ['xyn3037',]
	
	name = json.dumps(name)
	data = {}
	data['uids'] = name
	data['msg'] = msg

	url = 'http://192.168.40.111:10024/api/post_popo'
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	print content

def send_toqun_msg(msg):
	#name = ['xyn3037',]
	#print 'send ' + msg + 'to qun'
	
	
	data = {}
	#1079 is Eros group number
	data['uid'] = '1079092'
	#data['uid'] = '1339106'
	data['msg'] = msg

	url = 'http://192.168.40.111:10024/api/post_popo'
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()

	print content
import datetime
now = datetime.datetime.now()
timestr = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')	
def test_post():
	import urllib2
	import urllib
	data = {}
	data['starttime'] = '2017-05-23 00:00' 
	data['endtime'] = '2017-05-24 00:00' 
	
	url = 'http://192.168.40.195:8058/zz_list_info'
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	print type(content)
	
	content = json.loads(str(content))
	print content
	#for key in content['data']['data']['issues'][0]:
	#	print key,content['data']['data']['issues'][0][key]



def test_post2():
	import urllib2
	import urllib
	data = {}
	data['month'] = "201707"
	data['qaname'] = u"黄".encode('utf-8')
	url = "http://127.0.0.1:9010/alive"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	print content
def test_post3():
	import urllib2
	import urllib
	data = {"log":'#67923 【国家擂台赛】国家擂台赛玩法开发'}
	url = "http://192.168.40.159:8059/confirm_redmineid"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	print content
#test_post2()
print 'real'
test_post3()