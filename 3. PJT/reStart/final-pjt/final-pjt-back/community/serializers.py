from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at', 'user', 'like_users',)


class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    

    class Meta:
        model = Article
        fields = '__all__'


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at',)


class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = ('like_users',)
        read_only_fields = ('article',)


class UserCommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title',)
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'article',)
        
        
class RecommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'article', 'user', 'parent_comment',)
        read_only_fields = ('article', 'parent_comment',)