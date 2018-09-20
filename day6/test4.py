#在python3.3之后新增了asyncio模块，可以帮我们检测IO（只能是网络IO），实现应用程序级别的切换

import asyncio

@asyncio.coroutine
def task(task_id,senconds):
    print("%s is start"%task_id)
    yield from asyncio.sleep(senconds) #检测网络IO
    print("%s is end"%task_id)


tasks=[
    task(task_id='task1',senconds=3),
    task(task_id='task2',senconds=2),
    task(task_id='task3',senconds=1),
]

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()