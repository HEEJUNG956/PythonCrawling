from cgitb import html
import requests
from bs4 import BeautifulSoup

# naver 서버에 대화를 시도
response = requests.get("https://www.naver.com/")

# naver 에서 html 줌
html = response.text

# html 번역 선생님으로 수프 만듬
soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn 인거 한개만 찾아냄
word = soup.select_one('#NM_set_home_btn');

# 한개의 단어만 출력
print(word.text)