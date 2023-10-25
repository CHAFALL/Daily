# 1. 현재 폴더에서 django 프로젝트(my_pjt)와 앱(my_app)를 만들고 서버를 실행하기 위한 bash 명령어를 주석으로 작성하시오. 

# 가상 환경 venv 생성
# python -m venv venv

# 가상 환경 활성화
# source venv/Scripts/activate

# 장고 설치
# pip install django

# 의존성 파일 생성
# pip freeze > requirements.txt

# 프로젝트 생성
# django-admin startproject my_pjt .

# 앱 생성
# python manage.py startapp my_app

# 서버 실행
# python manage.py runserver

# 2. http://127.0.0.1:8000/hello로 받은 요청을 통해 my_app 앱의 views.py에 있는 hello 함수를 실행시킬 수 있도록 아래 urls.py를 작성하시오 
from django.urls import path
from my_app import views
urlpatterns = [
    path('hello/', views.hello)
]
