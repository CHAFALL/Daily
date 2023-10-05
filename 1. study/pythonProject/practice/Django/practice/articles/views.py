from django.shortcuts import render
import random
# Create your views here.
def index(request):
    context = {
        'name': 'Jane',
    }
    # 데이터를 Template로 보내겠다.
    # 또한, 데이터는 model에 접근해서 가져올 수도 있다.
    return render(request, 'articles/index.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    empty_list = []
    context = {
        'foods': foods,
        'picked': picked,
        'empty_list': empty_list,
    }
    return render(request, 'articles/dinner.html', context)


# throw로 부터 데이터를 받아서 써먹기(throw.html 참고하기)
def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)
