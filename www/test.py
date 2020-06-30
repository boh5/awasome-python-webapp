import asyncio
import inspect

from www import orm
from www.models import User


async def test(loop):
    await orm.create_pool(loop = loop, user='root', password='root', db='awesome')
    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
    await u.save()


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test(loop))
    r = inspect.signature(test)
    print(r)
