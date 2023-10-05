from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if product_price.get(thing) != None:
        total = product_price.get(thing) * cnt
    else:
        total = 0

    context={
        'thing': thing,
        # 'menu': product_price.keys,
        'cnt': cnt,
        'total': total
    }

    return render(request,'prices/price.html', context)
