from dotenv import load_dotenv
import os, requests, json
load_dotenv()
API_KEY = os.environ.get('VITE_TMDB_API_ACCESS_TOKEN')

def get_genre_data():
    total_data = []
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    genres = requests.get(url, headers=headers).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)
    
    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


def get_movie_data():
    total_data = []
    actor_data = []
    for i in range(1, 101):
        url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={i}"
        # url = f"https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page={i}"
        headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
        }
        movies = requests.get(url, headers=headers).json()

        for movie in movies['results']:
            credit_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?language=ko-KR"
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
            credits = requests.get(credit_url, headers=headers).json()
            actors = []
            for actor in credits["cast"][:20]:
                if actor.get('profile_path', ''):
                    actors.append(actor['id'])
                    actor_fields = {
                        'name': actor['name'],
                        'profile_path': actor.get('profile_path')
                    }
                    data = {
                        "pk": actor['id'],
                        "model": "movies.actor",
                        "fields": actor_fields
                    }
                    actor_data.append(data)
            if movie.get('release_date', ''):
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'actors': actors
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)



    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)
    with open("movies/fixtures/actor_data.json", "w", encoding="utf-8") as w:
        json.dump(actor_data, w, indent=4, ensure_ascii=False)


get_genre_data()
get_movie_data()