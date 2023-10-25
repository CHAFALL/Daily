from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        # model form이라서 우리가 기존에 사용했던 것 처럼 데이터가 젤 먼저 옴
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # 유저 객체가 어디에 있는가? 가 문제이다.
    # request.user에 있음, 그래서 굳이 몇번 유저인지 찾을 필요는 없음(회원 탈퇴를 누르는 사용자는 이미 요청 객체에 들어가 있음)

    # 회원탈퇴라는 것은 로그인 된 사용자가 본인이 눌러서 탈퇴를 하는 것, 그 로그인 된 사용자에 대한 정보가 request.user에 있음
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method =='POST':
        # 수정을 하는 원리는 똑같은데 articles와 다른 점은 articles는 어떤 것이 수정되는지 먼저 찾은 다음에 넣었다면,  user은 지금 상황에선 찾을 필요가 없음(어차피 회원정보 수정을 요청하는 이 요청객체에 이미 들어있기 때문)
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request,'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')

    else:
        form = PasswordChangeForm(request.user)
    context={
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)