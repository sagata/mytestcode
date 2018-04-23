#coding:utf-8
from xml.etree import ElementTree  
import re

print "tst"

root = ElementTree.parse("10240001.xml")
print type(root.find('regtask').find('rt_type').text)





root = ElementTree.parse("10250004.xml")
node_find = root.find('target_info')
target_node = node_find.find('target')
str2 = ''
str_count = 'ftcount'
str_key = 'ftca'
str2 = str2 + target_node.attrib.get('ftcamain')
for i in range(1,10):
	key = str_key + str(i)
	count = str_count + str(i)
	if target_node.attrib[key] != '':
		str2 = str2 + '+' + target_node.attrib[key] + '*' + target_node.attrib[count]
print str2


dict1 = {}
dict1[u'test'] = 'hehe'
print dict1

str1 = 'test'

print str1.decode('utf-8')

testdict = {'test':'hehe'}
if testdict.has_key('tes'):
	print "chenggong "





