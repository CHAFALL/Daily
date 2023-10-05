"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 패키지와 모듈의 개념이 들어감 여기서(폴더 위치 보면 알 수 있음)
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index),
    # articles라는 주소로 요청을 보내면, articles앱의 views에서 함수를 호출
    path('articles/', views.index),
    # 해당 주소로 왔을 때 어떠한 응답을 주겠다.
    # 콜백함수, articles를 만나면 실행
    # 어? 함수인데 괄호 안쓰네? 매개변수가 업다면 안 써유 여기선
    # 장고에선 끝나는 /빼먹으면 안됨
    
    
    
]
