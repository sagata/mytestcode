#coding=utf8
import json
import pickle 

class test(object):
	def  __init__(self):
		self.test = 'test'
	def hehe(self):
		print 'ded'
s = test()
print(json.dumps(s, default=lambda obj: obj.__dict__))