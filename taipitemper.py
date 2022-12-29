from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.cwb.gov.tw/V8/C/')

c = driver.find_element(By.CLASS_NAME, 'county-name')
print(c.text, end="")
a = driver.find_element(By.CLASS_NAME, 'low')
at = a.text.replace('\n', '')
print('溫度:'+at+'C')
