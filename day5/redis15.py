#发布者们
from redis14 import RedisHelper

import time

obj=RedisHelper()

while True:
    obj.public('hello redis!')
    time.sleep(5)