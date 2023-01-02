from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)
driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip004/tip421/dishes')

riceitem = driver.find_element(By.CLASS_NAME, 'pro-title')
print('便當名稱：'+riceitem.text)

riceprice = driver.find_element(By.CLASS_NAME, 'pro-amount')
print('便當價格：'+riceprice.text)

alldata = driver.find_elements(By.CLASS_NAME, 'main-tab-box tab-content')
ricetable = driver.find_elements(By.CLASS_NAME, 'pro-title')
riceprice = driver.find_elements(By.CLASS_NAME, 'pro-amount')
for item in alldata:
    item.find_element(By.CLASS_NAME, 'pro-title')
    item.find_element(By.CLASS_NAME, 'pro-amount')

    a = (item.text)
    print(a)

for itemprice in riceprice:
    price = (itemprice.text)
    print(price)


driver.close
