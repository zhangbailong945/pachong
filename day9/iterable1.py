import time

'''
def test():
    time.sleep(2)
    print('test is running!')

def deco(func):
    start=time.time()
    func()
    stop=time.time()
    print(stop-start)

deco(test)
'''


def timer(func):
    def deco():
        start=time.time()
        func()
        stop=time.time()
        print(stop-start)
    return deco

@timer
def test():
    time.sleep(2)
    print("test is running!")



test()
