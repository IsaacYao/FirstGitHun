# coding=utf-8
from selenium import webdriver
browser=webdriver.Firefox()
browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
name2=browser.title
name1=u'百度一下，你就知道'
print type(name2),len(name2),name2,type(name1),len(name1),name1
if name2 == u'百度一下，你就知道':
    print'success!'
else:
    print'failed!'
