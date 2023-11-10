<template>
  <div>
    <h1>MovieList</h1>
    
    <div v-for="movie in movies" :key="movie.id" >
      <card @click="goMovieDetail(movie)">
        <img v-if="movie.poster_path" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="#">
        <p>{{ movie.title }}</p>
        {{ movie }}
      </card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import router from '../router';

  const movies = ref([]);
  const moviesURL =
    'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko&page=1&sort_by=popularity.desc';

  const options = {
    headers: {
      accept: 'application/json',
      Authorization:
        'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MWM3MDQ2NmQ3ZjM3MGY2MWVhOTgyMGU5OWQ5ZTFjMiIsInN1YiI6IjY1NGRjYzdkNjdiNjEzMDBlNWRkNzZkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tPMsy8kiz31Ile1qXAIxdmA7XAzI4aYcl4bnFRlQDuQ',
    },
  };

  onMounted(() => {
    axios
      .get(moviesURL, options)
      .then((response) => {
        movies.value = response.data.results;
      })
      .catch((error) => {
        console.error(error);
      });
  });


  const goMovieDetail = (movie) => {
    router.push(`/${movie.id}`)
  }
</script>


<style scoped>
.card {
  display: flex;
}
</style>