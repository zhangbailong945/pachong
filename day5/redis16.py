#订阅者们
from redis14 import RedisHelper

obj=RedisHelper()
redis_sub=obj.subscribe()

while True:
    msg=redis_sub.parse_response()
    print(msg)