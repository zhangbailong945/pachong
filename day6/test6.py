import aiohttp
import asyncio

@asyncio.coroutine
def get_page(url):
    print('GEt:%s'%url)
    response=yield from aiohttp.request('GET',url)
    data=yield from response.read()
    print(url,data)
    response.close()
    return 1

tasks=[
    get_page('https://www.python.org'),
    get_page('https://www.cnblogs.com/linhaifeng'),
    get_page('https://www.openstack.org')
]

loop=asyncio.get_event_loop()
results=loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
print('=====>',results)