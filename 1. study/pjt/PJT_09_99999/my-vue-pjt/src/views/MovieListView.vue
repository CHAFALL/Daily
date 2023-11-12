<template>
  <div>
    <h1>MovieList</h1>
    <div v-if="movieIsEmpty">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
    <div v-else>
      <strong>로딩 중이거나, 영화 정보가 없습니다.</strong>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import MovieCard from '@/components/MovieCard.vue';
const router = useRouter()

const options = {
  method: 'GET',
  url: 'https://api.themoviedb.org/3/movie/top_rated',
  params: {language: 'ko', page: '1'},
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMGMxMjM4OGFhMmQ2NTBmMjhiZTMyYjAzYjEzODljYyIsInN1YiI6IjY1NGRjYzdkNjdiNjEzMDBlNWRkNzZkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hRWpp8ZeqNGb3PIzvP8rcNBag_RImk8YaYp9KWSQVKw'
  }
};

const movies = ref([])

axios
  .request(options)
  .then(function (response) {
    console.log(response.data.results);    
    movies.value = response.data.results
  })
  .catch(function (error) {
    console.error(error);
  });

// 로딩중이거나, 영화목록이 없을경우.
const movieIsEmpty = computed(()=>{
  return movies.value.length > 0 ? true : false
})

</script>

<style scoped>

</style>