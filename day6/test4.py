<<<<<<< HEAD
'''
上述无论哪种解决方案其实没有解决一个性能相关的问题：IO阻塞，无论是多进程还是多线程，
在遇到IO阻塞时都会被操作系统强行剥夺走CPU的执行权限，程序的执行效率因此就降低了下来。

解决这一问题的关键在于，我们自己从应用程序级别检测IO阻塞然后切换到我们自己程序的其他任务执行，
这样把我们程序的IO降到最低，我们的程序处于就绪态就会增多，以此来迷惑操作系统，
操作系统便以为我们的程序是IO比较少的程序，从而会尽可能多的分配CPU给我们，这样也就达到了提升程序执行效率的目的
'''

import asyncio
=======
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
>>>>>>> 676928e28053b4fa6d4176dc253eb8ec435aab63
