#coding:utf-8
import base64
f=open(r'C:\amhxy_resources_test\tcpout\avt\test\1.png','rb') #二进制方式打开图文件
print 'the first one'
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
#print ls_f
f.close()
f=open(r'C:\amhxy_resources_test\tcpout\avt\2.png','rb') #二进制方式打开图文件
ls_f2=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
print 'the second one'
#print ls_f2
if ls_f == ls_f2:
	print '1'
f.close()


import hashlib
def getFileMD5(filepath):
	f = open(filepath,'rb')
	md5obj = hashlib.md5()
	md5obj.update(f.read())
	hash = md5obj.hexdigest()
	f.close()
	return str(hash).upper()
	return None


print getFileMD5('1/testride.pal')
print getFileMD5('1/testride.pp')
print getFileMD5('1/testride.tcp')
print getFileMD5('2/testride.pal')
print getFileMD5('2/testride.pp')
print getFileMD5('2/testride.tcp')

import os
print os.listdir('1/img')
img1_path = '1/img'
img2_path = '2/img'
for filename in os.listdir('1/img'):
	img1 = img1_path + '/' + filename
	img2 = img2_path + '/' + filename
	base1 = base64.b64encode(open(img1,'rb').read())
	base2 = img2,base64.b64encode(open(img2,'rb').read())
	if base1 != base2:
		print filename


import json
tmp = ['fdaf']
json.dump(tnp)


CA = ('test1','test2')
print [{"filepath":{"regex":i+".*"}} for i in CA]