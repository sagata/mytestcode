# encoding=utf-8
import time
import json
'''
file2 = open('thefile.txt')


linecount = 0

while True:
 	time.sleep(1)

 	lines = file2.readlines()
 	if linecount == len(lines):
 		continue
	for i in range(linecount,len(lines)):
		print i,lines[i]
	linecount = len(lines)


'''
with open('thefile.txt','w') as f:
	f.write('test test')

with open('thefile.txt','r') as f:
	for each in f.readlines()[0].split(' '):
		print each


for i in range(9,10):
	print i
