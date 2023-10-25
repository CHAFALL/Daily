from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def push(request):
    context = {
        "name" : "choiyongsu",
    }
    return render(request, "articles/push.html", context)