<template>
  <div>
    <h1>MovieDetail</h1>
    {{ movie.title }}
    <img v-if="movie.poster_path" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="#">
    {{ movie.overview }}
    <button @click="watchPre"></button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const movie = ref([])
const movieId = route.params.movieId



const options = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${movieId}`,
  params: {language: 'ko'},
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MWM3MDQ2NmQ3ZjM3MGY2MWVhOTgyMGU5OWQ5ZTFjMiIsInN1YiI6IjY1NGRjYzdkNjdiNjEzMDBlNWRkNzZkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tPMsy8kiz31Ile1qXAIxdmA7XAzI4aYcl4bnFRlQDuQ'
  }
};

axios
  .request(options)
  .then(function (response) {
    console.log(response.data);
    movie.value = response.data
  })
  .catch(function (error) {
    console.error(error);
  });


</script>

<style scoped>

</style>