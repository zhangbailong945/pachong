import sys

'''
有GUI的测试工具
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
print(driver.page_source)


