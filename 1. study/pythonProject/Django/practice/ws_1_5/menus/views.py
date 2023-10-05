from django.shortcuts import render

# Create your views here.
foods = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
drinks = ["cider","coke","miranda","fanta", "eye of finetree"]

def food(request):
    context={
        'items': foods,
        'fnd': 'food',
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    context={
        'items': drinks,
        'fnd': 'drink',
    }
    return render(request, 'menus/drink.html', context)


def receipt(request):
    thing =  request.GET.get('thing').lower()
    fnd = request.GET.get('fnd')
    context = {
        'thing' : thing,
        'foods' : foods,
        'drinks' : drinks,
        'fnd' : fnd,
    }    
    return render(request,'menus/receipt.html', context)