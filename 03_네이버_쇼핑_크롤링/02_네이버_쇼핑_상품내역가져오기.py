from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#크롬 드라이버 자동업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip
import csv

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options=chrome_options)

#브라우저 생성
driver.get("https://www.naver.com")

#쇼핑 메뉴 클릭
driver.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = driver.find_element(By.CSS_SELECTOR, 'input._searchInput_search_text_3CUDs')
search.click()

#검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = driver.execute_script("return window.scrollY")

#무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

#파일 생성
f = open(r"D:\파이썬 크롤링\03_네이버_쇼핑_크롤링\data.csv", 'w', encoding='CP949', newline='')
                # 경로                                     쓰기모드    인코딩      줄바꿈제거
csvWriter = csv.writer(f)

# 상품 정보 div
items = driver.find_elements(By.CSS_SELECTOR, '.basicList_info_area__TWvzp')
print(items)

for item in items:
    name = item.find_elements(By.CSS_SELECTOR, 'basicList_title__VfX3c').text
    try:
        price = item.find_elements(By.CSS_SELECTOR, 'price_num__S2p_v').text
    except:
        price = "판매중단"
    link = item.find_elements(By.CSS_SELECTOR, 'basicList_title__VfX3c > a').get_attribute('href')
    print(name, price, link)
    #데이터쓰기
    csvWriter.writerow([name, price, link])


#파일닫기
f.close()
