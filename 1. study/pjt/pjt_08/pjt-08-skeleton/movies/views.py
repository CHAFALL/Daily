from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.all()
    
    recommended_movies = []
    for movie in movies:
        if movie.vote_count > 5000 and movie.vote_average > 8.3:
            recommended_movies.append((movie.popularity, movie.pk))
    
    recommended_movies.sort(reverse=True)
    recommended_movies = recommended_movies[:8]


    rcd_movies = []
    for i in recommended_movies:
        rcd_movies.append(Movie.objects.get(pk=i[1]))


    context = {
        'movies' : movies,
        'rcd_movies' : rcd_movies,
    }
    return render(request, 'movies/recommended.html', context)




# <p>제목 : {{movie.title}}</p>
# <p>발매일 : {{movie.release_date}}</p>
# <p>인기도 : {{movie.popularity}}</p>
# <p>추천 수 : {{movie.vote_count}}</p>
# <p>추천 평균 : {{movie.vote_average}}</p>
# <p>줄거리 : {{movie.overview}}</p>
# <img src="{{movie.poster_path}}" alt="영화사진">
# <p>장르 : {{movie.genres}}</p>