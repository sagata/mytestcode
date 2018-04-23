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
	data['starttime'] = '2017-08-31 00:00' 
	data['endtime'] = '2017-08-31 12:00' 
	data['search_type'] = 'open_bug' 
	#data['search_type'] = 'open' 
	#data['search_type'] = 'open' 
	
	url = 'http://192.168.40.195:8117/zz_list_info'
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	print type(content)
	
	content = json.loads(str(content))
	'''
	print content['data']['total_count']
	print content['data']['limit']
	print content['data']['offset']
	'''
	#print len(content['data'])
	for item in content['data']:
		print item['updated_on'][:10]
		#print item['created_on'][:9]
		#print item['assigned_to']['mail']
		#print item['status']['id']
		#print item['author']
		#break
	#for key in content['data']['data']['issues'][0]:
	#	print key,content['data']['data']['issues'][0][key]



def test_post2():
	import urllib2
	import urllib
	data = {}
	data['title'] = "[角色迭代][剑侠客]"
	data['status'] = '1'
	data['search_type'] = 'search_bug' 
	url = "http://192.168.40.195:8059/zz_list_info"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	content = json.loads(str(content))
	for item in content['data']:
		print item['subject'].encode('utf-8')

def get_gen_patch():
	data = {}
	url = "http://192.168.40.195:8015/get_now_regen"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	return content

def done():
	data = {}
	url = "http://192.168.40.195:8023/testtable/update_svn_tree"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	return content
def test8016():
	data = {}
	data['month'] = '201709'
	data['username'] = 'gzleyu' 
	url = "http://192.168.40.195:8016/get_stat_data"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	return content

def test8017():
	data = {}
	data['path'] = '0007\\fe' 
	url = "http://127.0.0.1:8010/gif_path"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	return content

def test80():
	data = {}
	url = "http://127.0.0.1:80"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	print content
	return content


import requests
POPO_API_URL = "http://192.168.40.159:9004/notify"
POPO_API_URL = "http://192.168.40.159:10024/api/post_popo"
def popo_to_group(group_id, message):
    payload = {
        "group": group_id,
        "msg": message
    }
    req = requests.get(POPO_API_URL, params=payload)



def popo_to_user(username, message):
    payload = {
        "urs": json.dumps(username),
        "msg": message
    }
    requests.get(POPO_API_URL, params=payload)


#popo_to_group(1289455,'test')
#print get_gen_patch()
'''
import os
command = 'ipconfig ' #可以直接在命令行中执行的命令
r = os.popen(command) #执行该命令
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    line = line.strip('\r\n')
    print line
'''
#popo_to_group(1289455,'test')

def sendPopo(uids, msg):
    POPO_API_URL = 'http://192.168.40.159:10024/api/post_popo'
    payload = {
        'uids': json.dumps(uids),
        'msg': msg,
    }
    ret = requests.get(POPO_API_URL, params = payload)
    print ret.status_code == 200

#sendPopo(['1423018'],'test')
#sendPopo(['xyn3037@corp.netease.com'],'fda')

def testcommit():
	data = {}
	data['month'] = '201709'
	data['username'] = 'gzleyu' 
	url = "http://192.168.40.159:8013/pre_commit"
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	content = req.read()
	return content


def testcommit2():

    pre_commit_url = 'http://192.168.40.159:8013/pre_commit'

    d = {u'change_list': 
    		[[u'U', u'osBranches/h45na/weekly/doc/_international/rea dme.txt'], [u'U', u'osBranches/h45na/weekly/version.txt'],
    		[u'U',u'osBranches/h45na/weekly/client/script/common/shared/switches_pc.py']
    		],
    	 u'txn': u'127310-35mq', 
    	 u'repos': u'1', 
    	 u'log': u'ref 23的',
    	 u'author': u'gzzhaoxing2014'
    	}
    
    data = json.dumps(d, ensure_ascii=True, encoding='utf-8')
    headers = {
        "Content-type": "application/json;charSet=utf-8",
        "Accept":"text/html;"
    }
    #print data
    req = urllib2.Request(pre_commit_url, data, headers)
    try:
        r = urllib2.urlopen(req, timeout=100)
    except:
        print 'urlopen fail or timeout'
        return 0
    #import time
    #time.sleep(1)

    pre_ret = str(r.read())

    print pre_ret
    print 'fs'
    #save_pre_ret(pre_ret_file, pre_ret)
    return 0 if pre_ret == '0' else 1
#print testcommit()
testcommit2()

