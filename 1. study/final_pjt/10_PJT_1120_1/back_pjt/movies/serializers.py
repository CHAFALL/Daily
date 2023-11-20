from rest_framework import serializers
from .models import Movie, Genre, MovieReview


class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'vote_avg','genres')
        read_only_fields = ('user',)

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