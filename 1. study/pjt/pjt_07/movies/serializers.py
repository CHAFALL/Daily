from rest_framework import serializers
from .models import Actor, Movie, Review

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')


# class 중복 제거를 위해 밖으로 빼둠!
class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)


class ReviewSerializer(serializers.ModelSerializer):
    
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('movie',)

class ActorSerializer(serializers.ModelSerializer):

    movies = MovieTitleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'
    


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')


class MovieSerializer(serializers.ModelSerializer):
    
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    
    
    actors = ActorNameSerializer(many=True, read_only=True)
    
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


