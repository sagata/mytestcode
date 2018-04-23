# -*- coding:utf-8 -*-


import os
import hashlib
def getFileMD5(filepath):
    
    f = open(filepath,'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()
    return None
alllist = []

for dirname in os.listdir(u"F:\\Test_version\\hutongbanshape\\all"):
	if dirname == ".svn":
		continue
	for key1,key2,key3 in os.walk(u"F:\\Test_version\\hutongbanshape\\all\\"+dirname):
		if ".svn" in key1:
			continue
		for filename in key3:
			filepath1 = key1 + "\\" + filename
			filepath2 = filepath1.replace('hutongbanshape','hutong125')
			#print filepath1
			#print filepath2
			if not os.path.exists(filepath2):
				if filepath2.endswith('.tcp'):
					print filepath2.replace(u"F:\\Test_version\\hutong125\\all\\","").encode('utf-8')
			continue
			if getFileMD5(filepath1) != getFileMD5(filepath2):
				#if '0002' in filepath1 or '0014' in filepath1:
				#	continue
				print filepath1.encode('utf-8') + ' md5'
				alllist.append(key1)

'''
for i in set(alllist):
	print i
'''
'''
count = 0
for key1,key2,key3 in os.walk(u"F:\\Test_version\\hutongbanshape"):
	if key1 == u"F:\\Test_version\\hutongbanshape":
		for filename in key2:
			filepath1 = key1 + "\\" + filename
			filepath2 = filepath1.replace('hutongbanshape','hutong125')
			if not os.path.exists(filepath2):
				count += 1
				print filename.encode('utf-8')
'''