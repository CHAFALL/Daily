<template>
  <div>
    <div v-if="genre">
      <h2 class="genre-name">{{ genre.name }}</h2>
    </div>
    <MovieList :movies="genreMovies"/>
    <progress class="progress" :value="scrollPercent" max="100"></progress>
  </div>
</template>


<script setup>

import MovieList from '@/components/Movie/MovieList.vue'
import { onMounted, onUnmounted, ref, watch, computed } from 'vue'
import { useMovieStore } from '@/stores/movies.js'
import { useRoute } from 'vue-router'
import axios from 'axios'

const movieStore = useMovieStore()
const route = useRoute()
const genreMovies = ref(null)
const scrollPercent = ref(0)

const genre = computed(() => {
  const genreId = parseInt(route.params.id)
  return movieStore.genres.find(genre => genre.id === genreId)
})

const fetchMovieData = function () {
  axios({
    method: 'get',
    url: `${movieStore.API_URL}/api/v1/movies/genres/${route.params.id}`
  })
    .then(res => {
      genreMovies.value = res.data
    })
    .catch(err => console.log(err))
}

const updateProgressBar = function () {
  const scrollTop = document.documentElement.scrollTop || document.body.scrollTop
  const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight
  scrollPercent.value = (scrollTop / windowHeight) * 100
}

onMounted(() => {
  movieStore.getGenres()
  fetchMovieData()
  window.addEventListener('scroll', updateProgressBar)
})

watch(() => route.params.id, () => {
  fetchMovieData()
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateProgressBar)
})

</script>


<style scoped>
.progress {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 5px;
  appearance: none;
  background: transparent;
  z-index: 1000;
}

.progress::-webkit-progress-bar {
  background: transparent;
}

.progress::-webkit-progress-value {
  background: linear-gradient(to right, lightgrey, #494949);
  border-radius: 5px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}

.genre-name {
  font-family: 'Noto Sans KR', sans-serif;
  text-align: center;
  margin-top: 50px;
  margin-bottom: 40px;
}
</style>

