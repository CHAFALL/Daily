from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
# Create your views here.
# get 요청과 post 요청이 create와 같이 둘 다 올 것이다.
# 로그인을 하기위한 페이지 리턴(get), 사용자가 id와 passward를 치고 post 요청으로 로그인 시도를 할 때(post)
def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 (세션 데이터 생성)
            auth_login(request,form.get_user())
            return redirect('articles:index')

    else:
        form = AuthenticationForm()
    context={
        'form': form, 
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')