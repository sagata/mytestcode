# -*- coding: utf-8 -*-
import re
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
#m = re.match(r'(\w+) (\w+)', 'hello world hello world')

#匹配对象
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
 
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')




if re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}","9999-00-00 00:00:00",):
	print 'fdaf'

#正则表达式对象
r = re.compile(r'(test)+')
m2 = r.findall('test232test')
print "r.findall ", m2
print "r.pattern", r.pattern
m2 = r.match('test232test')   #从一开始扫描找
print "r.match", m2
m2 = r.search('11test232test')  #整个string都扫描找
print "r.search", m2

tests = u'test\n\n[img]http://nos.netease.com/popo/79849541d656987ce0701de39936524c.png[/img] [img]http://nos.netease.com/popo/111.png[/img]'
r = re.compile(r'(\[img\]\S+\[\/img\])+')
m2 = r.findall(tests)
for item in m2:
	print item[5:-6]
print 'fsd'
print tests.replace("\[img\]\S+\[\/img\]","")

print '111'

if re.match(u".*[\u4e00-\u9fa5]+.*",u'osBranches/h45na/weekly/client/script/common/shared/switches_pc.py'):
	print 'fasdf'