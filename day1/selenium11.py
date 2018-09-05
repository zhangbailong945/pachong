## 获取当前网站的cookies

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 

chrome_options=Options()
chrome_options.add_argument('--headless')

chrome=webdriver.Chrome(chrome_options=chrome_options)
chrome.get('https://www.baidu.com')
time.sleep(4)
cookies=chrome.get_cookies()
print('Cookies:%s'% cookies)