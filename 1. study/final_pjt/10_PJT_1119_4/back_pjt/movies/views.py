from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

import requests
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer, MovieReviewSerializer
from .models import Movie , Genre, MovieReview
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


# 해당 리뷰에 대한 movie_review 생성 및 조회
@api_view(['GET','POST'])
def movie_review_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        movie_reviews = movie.moviereview_set.order_by('-pk')
        serializer = MovieReviewSerializer(movie_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        serializer = MovieReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 movie_review 조회, 수정 및 삭제
@api_view(['GET', 'DELETE', 'PUT'])
def movie_review_detail(request, movie_review_pk):
    movie_review = MovieReview.objects.get(pk=movie_review_pk)
    if request.method == 'GET':
        serializer = MovieReviewSerializer(movie_review)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = MovieReviewSerializer(movie_review, data=request.data)
        if not request.user.moviereviews.filter(pk=movie_review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            # 아래를 보면 moviereview 인스턴스에 이미 movie 데이터가 있어서 movie을 넘겨주지 않아도 됨을 알 수 있다.
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if not request.user.moviereviews.filter(pk=movie_review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        movie_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
































# @api_view(['GET', 'POST','PUT'])
# def takeGenre(request): 
#     if request.method == 'GET':
#         movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key=a0c12388aa2d650f28be32b03b1389cc&language=ko-KR'
#         genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=a0c12388aa2d650f28be32b03b1389cc'
#         genreList = requests.get(genreURL).json()
#         movieList = requests.get(movieURL).json()
#         genre = genreList.get('genres')
        
#     return Response(genre)



