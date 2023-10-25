from bs4 import BeautifulSoup
from selenium import webdriver

# g
# LC20lb MBeuO DKV0Md

# 최대한 공통적인 부분을 줄여주는 것이 검색할 때 유리

def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워진다!
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 결과물 제목들을 뽑아보자!
    # div 태그 중 g class들 가진 모든 요소 선택
    g_list = soup.select("div.g")
    for g in g_list:
        # 요소 안에 LC20lb MBeuO DKV0Md 를 가진 특정 요소
        title = g.select_one(".LC20lb MBeuO DKV0Md")
        # 결측시 처리
        if title is not None:
            print(f'제목={title.text}')


get_google_data('파이썬')