import sys,time,logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




#根据小说名搜索
def scrapy(url,keyword):
    chrome_options = Options()
    chrome_options.add_argument('window-size=800x600') #指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
    #chrome_options.add_argument('--headless') 
    chrome=webdriver.Chrome(chrome_options=chrome_options)

    chrome.get(url)
    #隐式等待
    chrome.implicitly_wait(3)
    try:
        #找到搜索栏
        search_input=chrome.find_element_by_id('sk')
        search_input.send_keys(keyword)
        #回车搜索
        search_input.send_keys(Keys.ENTER)

        get_result(chrome)
    except Exception as e:
        print(e)
    finally:
        chrome.close()


def get_result(chrome):
    chrome.implicitly_wait(3)
    try:
        #搜索列表
        book_list=chrome.find_elements_by_xpath('/html/body/div[3]/div[2]/ul')
        for book in book_list:
            book_name=book.find_element_by_class_name('.biaoti1')
            print(book_name.text)
            if book_name=='小说':continue
            book_name=book.find_element_by_class_name('.neirong1').text
            print(book_name)
    except Exception as e:
        print(e)
    finally:
        chrome.close()



def get_novel():
    pass


if __name__=='__main__':
    url='https://www.22ff.com'
    keyword='牧'
    scrapy(url,keyword)

