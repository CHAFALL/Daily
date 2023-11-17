from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

import requests
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer
from .models import Movie , Genre
from datetime import datetime

            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie(request) :
    if request.method == 'GET' :
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



# 장르 가져오기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genre(request) :
    if request.method == 'GET' :
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)




































# @api_view(['GET', 'POST','PUT'])
# def takeGenre(request): 
#     if request.method == 'GET':
#         movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key=a0c12388aa2d650f28be32b03b1389cc&language=ko-KR'
#         genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=a0c12388aa2d650f28be32b03b1389cc'
#         genreList = requests.get(genreURL).json()
#         movieList = requests.get(movieURL).json()
#         genre = genreList.get('genres')
        
#     return Response(genre)



