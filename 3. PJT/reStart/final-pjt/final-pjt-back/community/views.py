from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, UserArticleSerializer, CommentSerializer, UserCommentSerializer, RecommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if article.user == request.user:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    elif request.method == 'DELETE':
        if article.user == request.user:
            article.delete()
            return Response({'msg': f'{article_pk} deleted'}, status.HTTP_204_NO_CONTENT)
        

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        is_liked = article.like_users.filter(pk=request.user.pk).exists()
        context = {
            'isLiked': is_liked,
            'likeCount': article.like_users.count()
        }
        return JsonResponse(context)
    elif request.method == 'POST':
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False
        else:
            article.like_users.add(request.user)
            is_liked = True
        context = {
            'isLiked': is_liked,
            'likeCount': article.like_users.count()
        }
        return JsonResponse(context)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comment_like(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        is_liked = comment.like_users.filter(pk=request.user.pk).exists()
        context = {
            'isLiked': is_liked,
            'likeCount': comment.like_users.count()
        }
        return JsonResponse(context)
    elif request.method == 'POST':
        if comment.like_users.filter(pk=request.user.pk).exists():
            comment.like_users.remove(request.user)
            is_liked = False
        else:
            comment.like_users.add(request.user)
            is_liked = True
        context = {
            'isLiked': is_liked,
            'likeCount': comment.like_users.count()
        }
        return JsonResponse(context)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def recomment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(parent_comment=comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article, parent_comment=comment)
            return Response(serializer.data, status.HTTP_201_CREATED)
        

@api_view(['GET'])
def user_articles(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles = user.article_set.all()
    serializer = UserArticleSerializer(articles, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def user_comments(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    comments = user.comment_set.all()
    serializer = UserCommentSerializer(comments, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def like_articles(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), username=username)
        articles = user.like_articles.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)