#获取html标签属性

import sys
from selenium import webdriver
#chrome选项
from selenium.webdriver.chrome.options import Options
#模拟按键操作
from selenium.webdriver import ActionChains
#通过选择器、xpath等获取标签元素
from selenium.webdriver.common.by import By
#获取键盘按键
from selenium.webdriver.common.keys import Keys
#支持
from selenium.webdriver.support import expected_conditions as EC 
#等待页面元素加载
from selenium.webdriver.support.wait import WebDriverWait

chrome_options=Options()
#无边框的浏览器
chrome_options.add_argument('--headless')

#创建浏览器
chrome=webdriver.Chrome(chrome_options=chrome_options)
#访问地址
chrome.get('https://www.baidu.com')
#等待页面加载出来
wait=WebDriverWait(chrome,10)


try:
    wait.until(EC.presence_of_element_located((By.ID,'ftConw')))
    tag=chrome.find_element(By.CSS_SELECTOR,'#ftConw #lh #setf')

    #获取标签属性
    print(tag.get_attribute('href'))
    #获取标签位置x,y
    print(tag.location)
    #获取标签名字
    print(tag.tag_name)
    #获取标签的文字
    print(tag.text)
    #获取标签的大小w,h
    print(tag.size)
finally:
    chrome.close()


