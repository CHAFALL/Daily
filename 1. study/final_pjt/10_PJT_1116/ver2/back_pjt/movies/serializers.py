from rest_framework import serializers
from .models import Movie, Genre


class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title','poster_path','vote_avg')


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


