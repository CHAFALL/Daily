<template>
  <div class="container">
    <div class="movie-container">
      <div v-if="movie" class="movie-detail">
        <img :src="'https://image.tmdb.org/t/p/w342'+ movie.poster_path" style="width: 400px; height: auto; border-radius: 20px;">
        <div class="movie-info">
          <div class="group">
            <strong class="movie-title">{{ movie.title }}</strong>
            <img @click="openTrailerModal" style="width: 40px;" class="youtube" src="http://wiki.hash.kr/images/9/97/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EB%A1%9C%EA%B3%A0.png" alt="YouTube icon">
          </div>
          <div class="movie-genres">
            <span 
              v-for="genre in movie.genres" 
              :key="genre.id"
              class="genre"
              @click="router.push({name: 'genre', params:{id : genre.id}})"
              style="cursor: pointer;"
            >
              {{ genre.name }}
            </span>
          </div>
          <p class="movie-release-date">개봉일 : {{ movie.release_date }}</p>
          <div class="movie-rating">
            <p class="vote-count">평가 수 : {{ movie.vote_count }}</p>
            <div class="star-rating">
              <span v-for="n in Math.floor(movie.vote_average/2) *2 / 2" :key="n" class="star">★</span>
              <span v-for="n in 5 - Math.floor(movie.vote_average/2) *2 / 2" :key="n" class="star empty">☆</span>
            </div>
          </div>
          <p @click="like" style="width: 80px; cursor: pointer;" v-if="userStore.isLogin">{{ isLiked ? '❤️' : '🤍' }} 좋아요</p>
          <hr>
          <p class="movie-overview">{{ movie.overview }}</p>
          <hr>
        </div>
      </div>
      <br>
      <div class="movie-actors" style="width: 900px;">
        <h3>🎞️출연진🎞️</h3>
        <hr>
        <div class="carousel-container">
          <div class="carousel">
            <MovieDetailActors
              v-if="movie"
              :movieId="movie.id"
            />
          </div>
        </div>
      </div>
      <MovieDetailComment 
        v-if="movie && userStore.user"
        :voteCount="movie.vote_count" 
        :voteAvg="movie.vote_average" 
        :movieId="movie.id"
        @score-update="fetchMovieData"
      />
      <MovieDetailModal v-if="trailerModalOpen">
        <button @click="closeTrailerModal" class="close-button">❌</button>
        <iframe :src="youtubeVideoUrl" width="560" height="315" frameborder="0" allowfullscreen></iframe>
      </MovieDetailModal>
    </div>
  </div>
</template>



<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useMovieStore } from '@/stores/movies'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'
import MovieDetailModal from '@/components/Movie/MovieDetailModal.vue'
import MovieDetailActors from '@/components/Movie/MovieDetailActors.vue'
import MovieDetailComment  from '@/components/Movie/MovieDetailComment.vue'


const youtubeApiKey = import.meta.env.VITE_YOUTUBE_API_KEY
const moviestore = useMovieStore()
const userStore = useUserStore()
const route = useRoute()
const router = useRouter()
const movie = ref(null)
const trailerModalOpen = ref(false);
const youtubeVideoUrl = ref('');
const isLiked = ref(false)

onMounted(() => {
  fetchMovieData()
})

const fetchMovieData = function () {
  axios({
    method: 'get',
    url: `${moviestore.API_URL}/api/v1/movies/${route.params.id}/`,
  })
    .then(res => {
      movie.value = res.data
      for (const person of res.data.like_users) {
        if (person.username === userStore.user) {
          isLiked.value = true
        }
      }
    })
    .catch(err => console.log(err))
}

watch(() => route.params.id, () => {
  fetchMovieData()
})

const like = function () {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/api/v1/movies/${route.params.id}/like/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      isLiked.value = res.data.isLiked
    })
    .catch(err => console.log(err))
}

const openTrailerModal = () => {
  fetchYoutubeVideo();
  trailerModalOpen.value = true;
};

const closeTrailerModal = () => {
  trailerModalOpen.value = false;
};

const fetchYoutubeVideo = () => {
  const movieTitle = movie.value.title;
  const youtubeSearchUrl = `https://www.googleapis.com/youtube/v3/search?q=${encodeURIComponent(`${movieTitle} 예고편`)}&key=${youtubeApiKey}&part=snippet&type=video&maxResults=1`;

  fetch(youtubeSearchUrl)
    .then(response => response.json())
    .then(data => {
      const videoId = data.items[0]?.id.videoId
      if (videoId) {
        youtubeVideoUrl.value = `https://www.youtube.com/embed/${videoId}`
      }
    })
    .catch(error => {
      console.error('Error fetching YouTube video:', error)
    });
  };


  
</script>

<style scoped>
.container{
  display: flex;
  justify-content: center;
}
.movie-container {
  display: flex;
  flex-direction: column;
  border: 1px solid lightgray;
  padding: 20px;
  border-radius: 30px;
  width: 900px;
  align-items: center;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.6);
}

h2{
  display: inline-block;
}
.youtube{
  cursor: pointer;
}
.movie-detail {
  display: flex;
  align-items: center;
  font-family: 'Noto Sans KR', sans-serif;
}

.movie-detail img {
  width: 300px;
  height: auto;
  margin-right: 20px;
}

.movie-info {
  flex: 1;
}

.movie-title {
  font-size: 24px;
  font-weight: bold;
  margin-top: .5px;
  margin-right: 10px
}

.group{
  display: flex;
  
}

.movie-release-date {
  font-size: 16px;
  margin-bottom: 10px;
}

.movie-rating {
  display: flex;
  flex-direction: column;
  align-items: start;
  margin-bottom: 10px;
}

.star-rating {
  display: flex;
}

.star {
  color: gold;
}

.star.empty {
  color: lightgray;
}

.vote-count,
.vote-average {
  margin-right: 20px;
}

.movie-overview {
  letter-spacing: 0.3px;
  margin-bottom: 20px;
}

.movie-genres .genre {
  display: inline-block;
  margin-right: 10px;
  background-color: #f0f0f0;
  padding: 5px 10px;
  border-radius: 5px;
  font-family: 'Noto Sans KR', sans-serif;
}

</style>