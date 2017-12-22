#coding=utf8

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


class test(object):
	def __init__(self):
		print 'test'
	def go(self,g):
		print g

print dir(test)