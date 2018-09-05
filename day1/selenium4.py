## xpath的使用

import sys
from selenium import webdriver  #浏览器驱动
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains #模拟鼠标操作
from selenium.webdriver.common.by import By #根据什么获取元素对象
from selenium.webdriver.common.keys import Keys #键盘按键
from selenium.webdriver.support import expected_conditions as EC #断言中使用
from selenium.webdriver.support.wait import WebDriverWait  #等待页面加载某些元素
import time

chrome_options=Options()
#指定浏览器的分辨率
chrome_options.add_argument('window-size=1204x768')
#规避bug
chrome_options.add_argument('--disable-gpu')
#隐藏滚动条
chrome_options.add_argument('--hide-scrollbars')
#浏览器不提供可视化页面
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.baidu.com')
#显示等待页面加载
wait=WebDriverWait(driver,3)

try:
    #1.find_element_by_xpath
    #第一个//代表从整个html中寻找,之后的/代表子节点,之后//代码所有后代元素
    #driver.find_element_by_xpath('//body/a') 如果body没有子元素a，就会报错
    #driver.find_element_by_xpath('//body//a') #body之后的是a元素
    #driver.find_element_by_xpath('body a')  #body的兄弟节点
    #取第几个元素
    #alist=driver.find_elements_by_xpath('//body//a[1]') #去第二个a元素
    #print(alist[0].text)

    #2.按属性查找
    text1=driver.find_element_by_xpath('//a[5]')
    #根据href精确内容查找a元素
    text2=driver.find_element_by_xpath('//a[@href="https://www.hao123.com"]')
    #根据href模糊内容查找a元素
    text3=driver.find_element_by_xpath('//a[contains(@href,"hao123")]')
    print(text1.text)
    print(text2.text)
    print(text3.text)
    time.sleep(5)



finally:
    driver.close()


