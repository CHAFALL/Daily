from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    articles = Article.objects.all()
    content= {
        'articles' : articles
    }
    return render(request, 'articles/index.html', content)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    content = {
        'article' : article
    }
    return render(request, 'articles/detail.html', content)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    content = {
        'form' : form,
    }
    return render(request, 'articles/create.html', content)

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
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    content = {
        'form' : form,
        'article': article,
    }
    return render(request, 'articles/update.html', content)