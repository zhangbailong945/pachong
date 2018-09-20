import requests
import asyncio

@asyncio.coroutine
def get_page(func,*args):
    print('GET:%s'%args[0])
    loop=asyncio.get_event_loop()
    furture=loop.run_in_executor(None,func,*args)
    response=yield from furture

    print(response.url,len(response.text))
    return 1

tasks=[
    get_page(requests.get,'https://www.python.org/doc'),
    get_page(requests.get,'https://www.cnblogs.com/linhaifeng'),
    get_page(requests.get,'https://www.openstack.org')
]

loop=asyncio.get_event_loop()
results=loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

print('=====>',results)