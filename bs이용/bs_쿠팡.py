from math import prod
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet('식품')
wb.remove_sheet(wb['Sheet'])
ws.append(['이름','가격','배송기한','상세URL'])

i = 1

while True:

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument("ignore-certificate-errors");
    options.add_argument("--start-maximized") 
    options.add_argument("--window-size=1920,1080") 

    UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    options.add_argument('user-anget=' + UserAgent)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)


    driver.get(url= 'https://www.coupang.com/np/campaigns/82?page=' + str(i))
    time.sleep(5)
    try:
        product = driver.find_element(By.ID, 'productList')
        lis = product.find_elements(By.CLASS_NAME, 'baby-product')
        print('*' * 50 + ' ' + str(i) + '페이지 시작!' + ' ' + '*' * 50)
        
        for li in lis:
            try:
                product = li.find_element(By.CLASS_NAME, 'name').text
                price = li.find_element(By.CLASS_NAME, 'price-value').text
                delivery = li.find_element(By.CLASS_NAME, 'delivery').text
                url = li.find_element(By.CLASS_NAME, 'baby-product-link').get_attribute('href')

                print('Product: ' + product)
                print('price: ' + price)
                print('delivery: ' + delivery)
                print('url: ' + url)

                ws.append([product, price, delivery, url])

            except Exception:
                pass 

        print('*' * 50 + ' ' + str(i) + '페이지 끝!' + ' ' + '*' * 50)
        time.sleep(5)
        i += 1
        driver.quit()

    except NoSuchElementException:
        wb.save('D:/파이썬 크롤링/bs이용/쿠팡Test.xlsx')
        wb.close()
        exit(0)