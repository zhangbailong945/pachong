#发布订阅
import redis

class RedisHelper:

    def __init__(self):
        self.__conn=redis.Redis(host='localhost',port=6379,db=0)
        self.pub='fm97.8' #发布信息的频道名
        self.sub='fm97.8' #订阅信息的频道名
    
    def public(self,msg):
        self.__conn.publish(self.pub,msg) #向发布频道发布消息
        return True
    
    def subscribe(self):
        pub=self.__conn.pubsub() #拿到pub对象
        pub.subscribe(self.sub) #向订阅频道请求消息
        pub.parse_response()
        return pub