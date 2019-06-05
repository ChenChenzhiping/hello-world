#-*-coding:utf-8-*-
from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')


driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.baidu.com')
title = driver.title
print(title)
driver.quit()