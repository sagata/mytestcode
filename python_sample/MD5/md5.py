# -*- coding: utf-8 -*-
import hashlib
def getFileMD5(filepath):
    
    f = open(filepath,'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()
    return None


print getFileMD5('test.db')
import urllib2