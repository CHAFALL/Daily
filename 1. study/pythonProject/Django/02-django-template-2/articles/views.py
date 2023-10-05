import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
    'name' : 'jane',
    }

    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    # 첫번째 인자: request, 두번째 인자: 탬플릿 경로, 세번째 인자: context
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # 사용자로 부터 요청을 받아서
    # 요청에서 사용자 입력 데이터를 찾아
    # context에 저장 후 catch 템플릿에 출력
    # print(request)
    # print(type(request))
    # print(request.GET)
    # 객체 확인법(META)(모든 것들을 출력을 다 받아볼 수 있음)
    # print(request.META)
    # 호출 할 때 그냥 호출하는 것이 아니라 아까 url.py가 받았던 그 요청객체를 첫번째 인자가 매번 전달을 해주고 있었다.
    # 즉 request에 요청에 대한 모든 정보가 들어있다.
    # GET이라는 속성값에 원하는 것이 있어서 .GET으로 접근
    print(request.GET.get('message'))
    # 딕셔너리의 값 얻기(파이썬 문법)
    message = request.GET.get('message')
    # context에 message 저장
    context = {
        'message': message,

    }
    return render(request, 'articles/catch.html', context)
# name : url에 있는 변수를 받은 것이다.
def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)