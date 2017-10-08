#!/usr/bin/python
#coding=utf8
import asyncio
def hello_world(loop1):
    print('Hello World')
    loop1.stop()
loop1 = asyncio.get_event_loop()
# Schedule a call to hello_world()
loop1.call_soon(hello_world, loop1)
# Blocking call interrupted by loop1.stop()
loop1.run_forever()
loop1.close()

import asyncio
import datetime
def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()
loop = asyncio.get_event_loop()
# Schedule the first call to display_date()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)
# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()