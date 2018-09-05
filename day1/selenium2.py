import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options=Options()
#指定浏览器的分辨率
chrome_options.add_argument('window-size=1204x768')
#规避bug
chrome_options.add_argument('--disable-gpu')
#隐藏滚动条
chrome_options.add_argument('--hide-scrollbars')
#不加载图片，提升速度
chrome_options.add_argument('blink-settings=imageEnabled=false')
#浏览器不提供可视化页面
chrome_options.add_argument('--headless')
#启动失败调用谷歌浏览器,一般在不支持可视化的linux系统上
chrome_options.binary_location=r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

#初始化浏览器
chrome=webdriver.Chrome(chrome_options=chrome_options)
chrome.get('https://www.baidu.com')

print('登录' in chrome.page_source)

