from django.shortcuts import render
from datetime import datetime
# Create your views here.
def fruit(request):
    
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]
    context = {
        'fruit_list': fruit_list,
        'hate': hate,
    }
    
    
    return render(request, 'fruits/fruit.html', context)


def menu(request):
    menus = ['라면', '햄버거', '백반']
    users = []
    today = datetime.today
    context = {
        'menus': menus,
        'users': users,
        'today': today,
    }
    return render(request, 'menus/menu.html', context)