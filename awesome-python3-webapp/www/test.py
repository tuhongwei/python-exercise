import orm,asyncio
from models import User,Blog,Comment

async def test(loop):
	await orm.create_pool(loop,user='root',password='root',db='awesome')
	u1 = User(name='Test',email='1690542111@qq.com',passwd='1234567',image='about:blank')
	u2 = User(name='Administrator',email='admin@example.com',passwd='example',image='about:blank')
	await u1.save()
	await u2.save()
	await orm.destroy_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()