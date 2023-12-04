<template>
  <div v-if="movies">
      <h1 class="navbar">Recommended</h1>
      <h2>내가 좋아하는 장르의 영화</h2>
      <MovieRecommendList v-if="movies.genreMovies && movies.genreMovies.length > 0" :movies="movies.genreMovies"/>
      <div v-else>
        좋아요 한 영화가 없습니다.
        마음에 드는 영화에 좋아요를 눌러주세요.
      </div>
      <h2>평점이 높은 영화</h2>
      <MovieRecommendList :movies="movies.scoreMovies"/>
      <h2>리뷰 수가 많은 영화</h2>
      <MovieRecommendList :movies="movies.voteCountMovies"/>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import MovieRecommendList from '@/components/Movie/MovieRecommendList.vue'

const userStore = useUserStore()

const movies = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/movies/recommend/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      movies.value = res.data
    })
    .catch(err => console.log(err))
})

</script>

<style scoped>
 .navbar {
  margin-top: 50px;
 }
</style>