from django.shortcuts import render , redirect
# 여기도 살짝 기억
from .models import Article
# Create your views here.
def index(request):
    # 데이터베이스로부터 데이터 가져오기
    articles = Article.objects.all()
    content = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', content)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context={
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')

# 여기 기억하기!! (new로부터 데이터를 받아서 써먹기)
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # new로 부터 받아온 데이터를 통해 게시글 만들기
    article = Article(title=title, content=content)
    article.save()
    # 여기도 살짝 기억(redirect 모양)
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # db로 부터 데이터를 가져와서 지워버리기
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context={
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

# 여기 기억하기(여기 좀 어렵)
# create랑 느낌이 쪼매 다르네 article을 받고 그 다음에 그 속성에 대입하는 느낌
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 속성값을 이용함
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)