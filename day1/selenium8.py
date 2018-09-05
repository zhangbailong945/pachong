#执行js
import sys,time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait


chrome=webdriver.Chrome()
chrome.get('https://www.baidu.com')

chrome.implicitly_wait(3)
try:
    chrome.execute_script('alert("111111111")')
finally:
    chrome.close()