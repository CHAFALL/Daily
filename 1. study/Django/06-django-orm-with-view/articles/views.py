from django.shortcuts import render, redirect
from .models import Article

# 현재 위치에 있는 models에서 Article를 import 하겠다.

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,

    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # get의 특징: 단일 일때만 오류가 안남(반드시 한 개!)
    # article = Article.objects.get(id=pk) # 이것도 가능은 한데 안씀
    #왼쪽의 pk는 검색할 때 테이블의 열이름을 말하는 것이고 오른쪽의 pk는 variable routing을 통해서 온 변수의 이름이다.
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')



# 이부분 내가 지금 약함
# 데이터베이스에 게시글을 저장하는 역할을 해 줄 것이다.
# name속성으로 부터 받아옴
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2(이거 쓸 거임)(유효성 검사때문에 3번은 안 씀)(1번은 코드 김)
    article = Article(title=title, content=content)
    article.save()

    #3
    # Article.objects.create(title=title, content=content)


    # return render(request, 'articles/create.html')
    return redirect('articles:index')
    # 클라이언트에게 다시 요청을 보내라고 함
    # 어떤 주소로? articles의 index 주소로
    # render라고 하는 것은 말 그대로 템플릿을 만들어서 주는 것이다
    # 이번엔 redirect를 이용해보겠다.(다시 요청 보내기)
    # redirect는 CRUD 중 CUD에 이용됨(데이터 처리만 할 때??)

def delete(request, pk):
    # 몇 번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글을 삭제
    article.delete()
    # 페이지를 달라고 하는 요청이 아니라 데이터 다룸이 메인이었어서 redirect 해서 다른 페이지로 사용자를 보냄
    # 사용자를 보낸다 == 사용자가 GET 요청을 한번 더 보내도록 해야 한다.
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 수정하고자하는 게시글을 조회 # 여기 연구 필요(후반)(해결)
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)



# U로직도 C로직과 유사하다 다만, U로직은 새로운 인스턴스를 만들어가며 진행하는 것이 아니라
# 기존 인스턴스를 먼저 찾고 기존의 게시글에다가 새로운 값으로 갱신 시켜주는 점이 다르다. 