<template>
  <div>
    <h1>MovieDetail</h1>
    <div>
      <img v-if="movie.poster_path" :src = "`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="#">
      <h5>{{ movie.title }}</h5>
      <p>개봉일 : {{ movie.release_date }}</p>
      <p>러닝타임 : {{ movie.runtime }}</p>
      <p>TMDB 평점 : {{ movie.vote_average }}</p>
      <h5>장르</h5>
      <div v-for="genre in movie.genres" :key="genre.id">
        <span>{{ genre.name }}</span>
      </div>
      <h5>줄거리</h5>
      <p>{{ movie.overview }}</p>
      <h5>공식 예고편</h5>
      <!-- Button to open Bootstrap modal -->
      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#trailerModal">
        Watch Trailer
      </button>
      <!-- Bootstrap Modal -->
      <div class="modal fade" id="trailerModal" tabindex="-1" aria-labelledby="trailerModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="trailerModalLabel">Official Trailer</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <!-- Add your trailer iframe or video embed code here -->
              <!-- For example, you can embed a YouTube video: -->
              <iframe width="100%" height="315" :src="`https://www.youtube.com/embed/${movieYoutubeId}`" frameborder="0" allowfullscreen></iframe>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const movieId = route.params.movieId

const options = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${movieId}`,
  params: {language: 'ko'},
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMGMxMjM4OGFhMmQ2NTBmMjhiZTMyYjAzYjEzODljYyIsInN1YiI6IjY1NGRjYzdkNjdiNjEzMDBlNWRkNzZkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hRWpp8ZeqNGb3PIzvP8rcNBag_RImk8YaYp9KWSQVKw'
  }
};

const movie = ref([])

axios
  .request(options)
  .then(function (response) {
    console.log(response.data);
    movie.value = response.data
    
  })
  .catch(function (error) {
    console.error(error);
  });


const movieYoutubeId = ref('')


  const options2 = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${movieId}/videos`,
  params: {language: 'ko'},
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMGMxMjM4OGFhMmQ2NTBmMjhiZTMyYjAzYjEzODljYyIsInN1YiI6IjY1NGRjYzdkNjdiNjEzMDBlNWRkNzZkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hRWpp8ZeqNGb3PIzvP8rcNBag_RImk8YaYp9KWSQVKw'
  }
};

axios
  .request(options2)
  .then(function (response) {
    console.log(response.data.results[0].key);
    movieYoutubeId.value = response.data.results[0].key
  })
  .catch(function (error) {
    console.error(error);
  });


</script>

<style scoped>

</style>