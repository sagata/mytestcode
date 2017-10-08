#!/usr/bin/python
#coding=utf8
import asyncio
 
async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)

def done_callback(futu):
    print('Done')

loop = asyncio.get_event_loop()
futu = asyncio.ensure_future(do_some_work(3))
futu.add_done_callback(done_callback)
loop.run_until_complete(futu)