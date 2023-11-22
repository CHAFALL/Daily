<template>
  <h1 class="movie-title">{{ movie?.title }}</h1>
  <div class="movie-detail">
  
    <!-- 포스터 -->
    <div class="left-column">
      <img v-if="movie && movie.poster_path" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="#">
    </div>
    <div class="center-column">
      <p class="movie-rating">평점 : {{ movie?.vote_avg }}</p>
      <!-- Add like button/icon and show like status -->
      <button @click="toggleLike" 
      :class="{ 'liked': isLiked, 'not-liked': !isLiked }">
      {{ isLiked ? 'Unlike' : 'Like' }}
      </button>
      
      <!-- Add interest button/icon and show interest status -->
      <button @click="toggleInterest" 
      :class="{ 'not-interested': isUnInterested, 'interested': !isUnInterested }">
      {{ isUnInterested ? 'Interested' : 'Uninterested' }}
      </button>
      <br>
      <h3 style="color: aliceblue;">장르</h3>
      <hr>
      <div v-for="genre in movie?.genres" :key="genre.id">
        <span class="genre-name">{{ genre.name }}</span>
      </div>
      <br>
      <h3 style="color: aliceblue;">줄거리</h3>
      <hr>
      <p class="movie-overview">{{ movie?.overview }}</p>
      <!-- 유튜브 이동 -->
      <button @click="toggleVideoPlay" style="color: azure;">트레일러 보기</button>
      <template v-if="isPlaying"> 
        <iframe width="100%" height="315" :src="`https://www.youtube.com/embed/${movieYoutubeId}`" frameborder="0" allowfullscreen></iframe>
      </template>
      
    </div>
    <!-- 리뷰 -->
    <div class="right-column">
      <MovieReviewForm :movie="movie" />
      <MovieReviewList :movie="movie" />
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import MovieReviewForm from '@/components/MovieReviewForm.vue';
import MovieReviewList from '@/components/MovieReviewList.vue';

const route = useRoute();
const store = useCounterStore();

const movie = ref(null);
const isLiked = ref(null);
const isUnInterested = ref(null);
const isPlaying = ref(false)
const genres = ref([])


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data.genres);
      console.log(res);
      movie.value = res.data;
      genres.value = res.data.genres.map(genre => genre.name);
      // genres.value = res.data.genres

      console.log(genres.value)

      // 장르 데이터 가져오기
      return axios({
        method: 'post',
        url: `${store.API_URL}/api/v1/get_genres/`,
        headers: {                                  // 토큰 인증
        Authorization: `Token ${store.token}`     
        },
        data:{
          genres: genres.value
        }
      });
    })
    .then((res) => {
      console.log(res);
      // 여기서 장르 데이터 처리
    })
    .catch((err) => {
      console.log(err);
    });
});



onMounted(()=>{
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/likes/`,
    headers: {                                  // 토큰 인증
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      // Update the like status based on the response
      isLiked.value = res.data.is_liked;

    })
    .catch((err) => {
      console.log(err);
    });

  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/interests/`,
    headers: {                                  // 토큰 인증
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      // Update the like status based on the response
      isUnInterested.value = res.data.is_uninterested;

    })
    .catch((err) => {
      console.log(err);
    });
})


const toggleLike = () => {
  
  // Make a request to your backend to update the like status
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/likes/`,
    headers: {                                  // 토큰 인증
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      // Update the like status based on the response
      isLiked.value = res.data.is_liked;

    })
    .catch((err) => {
      console.log(err);
    });
};

const toggleInterest = () => {
  
  // Make a request to your backend to update the like status
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/interests/`,
    headers: {                                  // 토큰 인증
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      // Update the like status based on the response
      isUnInterested.value = res.data.is_uninterested;
      store.getMovies()

    })
    .catch((err) => {
      console.log(err);
    });
};

const toggleVideoPlay = function () {
  isPlaying.value = !isPlaying.value
}


const movieYoutubeId = ref('')

  const options = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${route.params.id}/videos`,
  params: {language: 'ko'},
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMGMxMjM4OGFhMmQ2NTBmMjhiZTMyYjAzYjEzODljYyIsInN1YiI6IjY1NGRjYzdkNjdiNjEzMDBlNWRkNzZkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hRWpp8ZeqNGb3PIzvP8rcNBag_RImk8YaYp9KWSQVKw'
  }
};

axios
  .request(options)
  .then(function (response) {
    console.log(response.data.results[0].key);
    movieYoutubeId.value = response.data.results[0].key
  })
  .catch(function (error) {
    console.error(error);
  });




</script>

<style scoped>
.movie-detail {
  display: flex;
  justify-content: space-around;
}

.left-column {
  text-align: center;
  background-color: black;
}

.center-column {
  background-color: black;
  width: 500px;
  min-width: 500px;
  padding: 20px;
}
.right-column {
  background-color: black;
  width: 600px;
  min-width: 600px;
  padding: 40px;
}

.movie-title {
  background-color: black;
  text-align: center;
  font-size: 50px; /* 원하는 글씨 크기 설정 */
  color: #f1eded; /* 원하는 글씨 색상 설정 */
}

.movie-rating {

  font-size: 20px; /* 원하는 글씨 크기 설정 */
  color: #007BFF; /* 원하는 글씨 색상 설정 */
}

.genre-name {
  
  font-size: 16px; /* 원하는 글씨 크기 설정 */
  color: #28A745; /* 원하는 글씨 색상 설정 */
}

.movie-overview {
  
  font-size: 20px; /* 원하는 글씨 크기 설정 */
  color: #6C757D; /* 원하는 글씨 색상 설정 */
}


/* Style for the like button/icon */
.liked {
  color: #dc3545; /* Change color to red when liked */
  margin-right: 25px;
}

.not-liked {
  color: #28A745; /* Change color to green when not liked */
  margin-right: 25px;
}

.interested {
  color: #dc3545; /* Change color to red when interested */
  margin-right: 25px;
}

.not-interested {
  color: #28A745; /* Change color to green when not interested */
  margin-right: 25px;
}
@media (max-width: 800px) {
  .movie-detail {
    flex-direction: column;
  }

  .left-column,
  .center-column,
  .right-column {
    width: 100%;
  }
}

</style>
