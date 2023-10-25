from django.shortcuts import render

# Create your views here.
def first(request):
    message = request.GET.get('message', '아무것도 받지 못함')
    context = {
        'message': message,
    }
    return render(request,'throw_catch/first.html', context)

def second(request):
    message = request.GET.get('message', '아무것도 받지 못함')
    context = {
        'message': message,
    }
    return render(request,'throw_catch/second.html', context)
