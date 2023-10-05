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
#     form = ArticleForm()
#     context={
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    # 요청의 메서드가 POST라면(create)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사 진행
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            article = form.save() # save에 리턴 기능이 있음
            return redirect('articles:detail', article.pk)
        # 중복이라 지움(아래)
        # 유효성 검사가 통과하든 못하든 넘어가는 데 통과 못하면 실패한 이유가 담긴 form이 넘어감
        # context = {
        #     'form': form,
        # }
        # return render(request, 'articles/new.html', context)
    # 요청의 메서드가 POST가 아니라면(new)
    else:
        form = ArticleForm()
    # 한 칸 앞으로 (같이 쓸려고)(아래)
    context={
        'form': form,
    }
    return render(request, 'articles/create.html', context)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     # 초기값 넣어주기(instance)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

# create와 update의 차이점은 instance 밖에 없음 이걸로 생성과 수정 판단
def update(request, pk):
    # 최상단으로 빼줌(아래)
    article = Article.objects.get(pk=pk)
    # 요청 메서드가 POST라면 (update)
    if request.method == 'POST':
        # 기준을 위해서 instance 넣어줘야 됨 이걸 보고 수정인지 판단
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            # save가 되는 것은 2가지다 -> 생성, 수정
            # 이 두가지를 판단 할 기준이 필요
            form.save() # 위에 article객체가 있어서 굳이 여기서 저장한 객체를 담아줄 필요는 x
            return redirect('articles:detail', article.pk)
        # context = {
        #     'form':form,
        # }
        # return render(request, 'articles/edit.html', context)
    # 요청의 메서드가 POST가 아니라면(edit)
    else:
        # article = Article.objects.get(pk=pk)
        # 초기값 넣어주기(instance)
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
