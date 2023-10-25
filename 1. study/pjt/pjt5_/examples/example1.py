from bs4 import BeautifulSoup
from selenium import webdriver

# 자바 스크립트가 모두 동작한 후의 최종 결과물을 가져와야 된다.(왜? 내가 request를 통해서 받아온 후로 페이지를 변경시켜주는 과정에서 우리랑 다른 결과물(ex)class명이 다름)을 볼 수 o)

def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워진다!
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")


    # 검색 결과 가져오기
    # div 태그 안의 id가 result=stats 라는 요소
    result_stats = soup.select_one("div#result-stats")
    print(result_stats.text)

    # 최대한 공통적인 부분을 줄여주는 것이 검색할 때 유리



    

get_google_data('파이썬')