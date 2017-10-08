#!/usr/bin/python
#coding=utf8
import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

## 3.5 以后的新语法
'''
async def hello2():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

loop2 = asyncio.get_event_loop()
tasks2 = [hello2(), hello2()]
loop2.run_until_complete(asyncio.wait(tasks2))
loop2.close()

'''