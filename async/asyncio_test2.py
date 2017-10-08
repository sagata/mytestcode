#!/usr/bin/python
#coding=utf8
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    print('connect finish %s...' % host)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    print('writer finish %s...' % host)
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        #print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    print('##########print finish %s...' % host)
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

def fib():
	test = yield from [11,22,33]
	print(test)
f = fib()
for i in f:
	print(i)