#浏览器标签页处理
import time
from selenium import webdriver

chrome=webdriver.Chrome()
chrome.get('https://www.baidu.com')
#执行JS
chrome.execute_script('window.open()')

#获取所有的选项卡
print(chrome.window_handles)
#切换到第2个选项卡
chrome.switch_to_window(chrome.window_handles[1])
chrome.get('https://www.tmall.com')
time.sleep(3)
#切换到第一个选项卡
chrome.switch_to_window(chrome.window_handles[0])
chrome.get('https://www.sina.com.cn')
time.sleep(2)
chrome.close()