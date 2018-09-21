##项目目录以及爬虫应用简介
project_name/
    scrapy.cfg
    project_name/
    __init__.py
    items.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...
        spidern.py

文件说明：
scrapy.cfg 项目的主配置信息，部署scrapy时使用，爬虫相关的配置信息在settings.py文件中
items.py 设置数据存储模板，用于结构化
pipelines 数据处理行为，一般结构化的数据持久化
settings.py 爬虫配置文件，如：并发数，延迟下载等
spiders 爬虫目录，如：创建文件，爬虫规则



#在项目目录下新建：entrypoint.py
from scrapy.cmdline import execute
execute(['scrapy','scrawl','scrapy1'])

#windows编码
import sys,os
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
