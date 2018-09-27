#item pipeline类
#1.如果优先级高的Pipeline的process_item返回一个值或者None，会制动传给下一个pipeline的process_item
#2.如果只想让第一个Pipeline执行，那得让一个pipeline的process_item抛出异常raise DropItem()
#可以用spider.name=='爬虫名' 来控制哪些爬虫pipeline


from scrapy.exceptions import DropItem

class CustomerPipeline(object):

    def __init__(self,v):
        self.value=v
    
    @classmethod
    def from_crawler(cls,crawler):
        '''
        scrapy会先通过getattr判断我们是否自定义了from_crawler，有则调用它来完成实例化
        '''
        val=crawler.settings.getint('MMMM')
        return cls(val)
    
    def open_spider(self,spider):
        '''
        爬虫刚启动时执行一次
        '''
        print('start')
    
    def close_spider(self,spider):
        '''
        爬虫关闭时执行一次
        '''
        print('end')
    
    def process_item(self,item,spider):
        #操作进行持久化操作
        #return 表示会被后续的pipeline继续处理
        return item
        #表示将item丢弃，不会被后续的pipeline处理
        #raise DropItem()