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

def get_url():
	url = 'http://192.168.40.195:19119/dashboard/obj_check?id=19751'
	params = urllib.urlencode({'id': 2213123123})
	print "http://192.168.40.195:19119/dashboard/obj_check?%s" % params
	f = urllib.urlopen("http://192.168.40.195:19119/dashboard/obj_check?%s" % params)
	print f.read()

def get_url2():
	url = 'http://192.168.40.195:8023/work_console/get_weekqa_by_console/'
	f = urllib.urlopen(url)
	print f.read()

import time
def get_url3():
	url = 'http://192.168.47.101:5000/stop'
	f = urllib.urlopen(url)
	print f.read()
	time.sleep(2)
	url = 'http://192.168.47.101:5000/start'
	f = urllib.urlopen(url)
	print f.read()

get_url3()