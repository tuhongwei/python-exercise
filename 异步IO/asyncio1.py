import asyncio,threading

@asyncio.coroutine
def hello():
	print("Hello world! %s" % threading.currentThread())
	r = yield from asyncio.sleep(1)
	print("Hello again! %s" % threading.currentThread())

tasks = [hello(),hello()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()