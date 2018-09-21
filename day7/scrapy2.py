#牛刀小试

#创建scrapy项目
scrapy startproject scrapy1

cd scrapy1

#创建爬虫
scrapy gensipder baidu www.baidu.com 

#查看配置文件
scrapy settings --get xxx

#调试
scrapy shell https://www.baidu.com

#检测内容是否是ajax请求实现的
scrapy view https://www.taobao.com

#爬虫页面，拿到请求头
scrapy fetch --nolog --headers https://www.taobao.com

#scrapy 版本
scrapy version

#scrapy 依赖库
scrapy version -v

#进入项目后执行的命令
scrapy crawl baidu

#检测项目是否有语法错误
scrapy check 

#获取爬虫列表
scrapy list

#检测解析的地址有无回调函数
scrapy parse https://www.taobao.com/ --callback parse

#压力测试
scrapy bench


