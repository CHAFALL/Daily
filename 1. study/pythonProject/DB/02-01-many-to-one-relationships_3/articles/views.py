from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 역참조: 이 게시물에 등록된 모든 댓글
    comments = article.comment_set.all()
    comment_count = article.comment_set.count()
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

# POST로만 요청을 받음
def comments_create(request, pk):
    # 게시글 조회(댓글을 생성하는데 왜 게시글 조회를?, 댓글 생성할 때 어떤 게시글에 달리는지를 할당해줘야 해서)
    article = Article.objects.get(pk=pk)
    # CommentForm으로 사용자로 부터 데이터를 입력 받음
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 우리가 필요한 것은 comment(댓글 인스턴스)이다.
        # 필요한 것이 있으면 더 넣어라.(commit=False의 역할)
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'comment_form':comment_form,
    }
    return render(request, 'articles/detail.html', context)

