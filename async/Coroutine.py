#!/usr/bin/python
#coding=utf8
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)




def receiver():
    print 'ready to receive'
    while True:
        n = (yield)
        print 'receive ' + n 

r = receiver()
r.next()   # 这样也可以 r.send(None)
r.send('1')