from rest_framework import serializers
from .models import Movie, Genre, MovieReview
from django.contrib.auth import get_user_model

# 커스텀 유저 모델에 대한 Serializer
class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class MovieListSerializer(serializers.ModelSerializer):
    

    # UserSerializer를 사용하여 like_users 정보를 포함

    # 이거 때문에 개고생했네!!!!
    # like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'vote_avg','genres','like_users', 'uninterest_users', 'overview')
        # read_only_fields = ('user',)



class MovieSerializer(serializers.ModelSerializer):
    
    # overriding    
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    
    genres = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'id')


class MovieReviewSerializer(serializers.ModelSerializer):
    
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = MovieReview
        fields = ('id', 'content', 'created_at','updated_at', 'user_name', 'rank')
        read_only_fields = ('movie', 'user')



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'genre_dict')