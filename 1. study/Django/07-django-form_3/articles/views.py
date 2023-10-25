from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm() # 인스턴스 생성
#     context={
#         'form':form,
#     }
#     return render(request, 'articles/new.html', context)

# 왜 get으로 if문 할 수 있는데 안함?
# get, post 말고도 다른 것이 있는데 아래의 구문은 반드시 POST여야만 하는 구문이라서 그럼

def create(request):
    # 요청의 메서드가 POST라면(create)
    if request.method == 'POST':
        form = ArticleForm(request.POST) # 아래처럼 받을 필요 없이 통으로 받을 수 있다.(@)
        # 유효성 검사
        if form.is_valid():
            article = form.save() #이 save엔 리턴이 있다.
            return redirect('articles:detail', article.pk)
        # 여기에 실패한 이유가 담긴 form이 포함된다.(아래)
        # context={
        #     'form':form,
        # }
        # return render(request, 'articles/new.html', context)
    # 요청의 메서드가 "POST가 아니라면"(new)
    else:
        form = ArticleForm() # 인스턴스 생성
    context={
    'form':form,
    }
    return render(request, 'articles/create.html', context)

    #(@)
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    # return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    # edit은 초기값으로 기존 데이터가 있어줘야 한다.(아래)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form':form,
    }
    return render(request, 'articles/update.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청 메서드가 POST라면(update)
    if request.method =='POST':
        # save()에서 수정임을 알려주기 위함으로 instance를 넣어줘야 됨
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
        # context={
        #     'form':form,
        # }
        # return render(request, 'articles/edit.html', context)
    # 요청 메서드가 POST가 아니라면(edit)
    else:
        # article = Article.objects.get(pk=pk)
        # edit은 초기값으로 기존 데이터가 있어줘야 한다.(아래)
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form':form,
    }
    return render(request, 'articles/update.html', context)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
