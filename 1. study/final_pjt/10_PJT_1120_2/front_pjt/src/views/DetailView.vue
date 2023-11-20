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
      <button @click="toggleLike" :class="{ 'liked': isLiked }">
        {{ isLiked ? 'Unlike' : 'Like' }}
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
const isLiked = ref(false);

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data);
      movie.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});

const toggleLike = () => {
  // Toggle the like status
  isLiked.value = !isLiked.value;

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




</script>

<style scoped>
.movie-detail {
  display: flex;
  justify-content: space-between;
}

.left-column {
  text-align: center;
  background-color: black;
  flex: 2;
}

.center-column {
  background-color: black;
  flex: 1;
  padding: 20px;
}
.right-column {
  background-color: black;
  flex: 2;
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
}

</style>
