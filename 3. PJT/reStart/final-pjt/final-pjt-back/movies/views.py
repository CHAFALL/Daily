from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Movie, Genre, MovieComment, Actor
from .serializers import MovieListSerializer, MovieDetailSerializer, GenreSerializer, MovieCommentSerializer, ActorSerializer


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
    if request.method == 'GET':
        score_movies = Movie.objects.order_by('-vote_average')
        score_movies = score_movies[:100]
        vote_count_movies = Movie.objects.order_by('-vote_count')
        vote_count_movies = vote_count_movies[:100]

        liked_movies = request.user.like_movies.all()
        if request.user.like_movies.all().exists():
            cnt = {}
            for movie in liked_movies:
                genres = movie.genres.all()
                for genre in genres:
                    cnt[genre.pk] = cnt.get(genre.pk, 0) + 1
            genre_pk = max(cnt.items(), key=lambda x: x[1])[0]
            genre = get_object_or_404(Genre, pk=genre_pk)
            genre_movies_list = genre.movie_set.order_by('-vote_average')
            i = 0
            genre_movies = []
            while i < len(genre_movies_list) and len(genre_movies) < 11:
                temp = genre_movies_list[i]
                if not temp.like_users.filter(pk=request.user.pk).exists():
                    genre_movies.append(temp)
                i += 1
        else:
            genre_movies = {}
        score_serializer = MovieListSerializer(score_movies, many=True)
        vote_serializer = MovieListSerializer(vote_count_movies, many=True)
        genre_serializer = MovieListSerializer(genre_movies, many=True)
        context = {
            'scoreMovies': score_serializer.data,
            'voteCountMovies': vote_serializer.data,
            'genreMovies': genre_serializer.data,
        }
        return Response(context)


@api_view(['GET'])
def get_genre_movies(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    movies = genre.movie_set.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    movies = actor.movie_set.all()
    actor_serializer = ActorSerializer(actor)
    movie_serializer = MovieListSerializer(movies, many=True)
    context = {
        'actor': actor_serializer.data,
        'movies': movie_serializer.data
    }
    return JsonResponse(context)


@api_view(['GET'])
def movie_search(request, word):
    movies = Movie.objects.filter(title__contains=f"{word}")
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_actors(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    actors = movie.actors.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            is_liked = False
        else:
            movie.like_users.add(request.user)
            is_liked = True
        context = {
            'isLiked': is_liked,
            'likeCount': movie.like_users.count()
        }
        return JsonResponse(context)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def movie_scores(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'PUT':
        serializer = MovieDetailSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_comments(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        comments = movie.comments.all()
        serializer = MovieCommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status.HTTP_201_CREATED)
        

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def movie_comments_detail(request, movie_pk, comment_pk):
    comment = get_object_or_404(MovieComment, pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer = MovieCommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def like_movies(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), username=username)
        movies = user.like_movies.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

