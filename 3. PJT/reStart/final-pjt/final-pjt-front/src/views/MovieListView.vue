<template>
  <div>
    <div class="align">
    <h1 class="navbar" style="margin-top: 50px;">MovieList</h1>
    <form @submit.prevent class="search">
      <input class="search-input" type="text" id="search-bar" v-model="searchWord" autocomplete="off" required>
      <label>search</label>
    </form>
    <div class="genre-btn">
        <span></span>
      <br>
      <MovieGenreList/>
    </div>
    <br>
  </div>
    <MovieList :movies="isSearch ? movies : moviestore.movies "/>
    <progress class="progress" :value="scrollPercent" max="100"></progress>
  </div>
</template>

<script setup>
import MovieList from '@/components/Movie/MovieList.vue'
import MovieGenreList from '@/components/Movie/MovieGenreList.vue';
import { onMounted, onUnmounted, ref, watch, computed } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movies.js'

const moviestore = useMovieStore()
const scrollPercent = ref(0)
const movies = ref(null)
const searchWord = ref(null)

onMounted(() => {
  moviestore.getMovies()
  movies.value = moviestore.movies
  window.addEventListener('scroll', updateProgressBar)
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateProgressBar)
})

function updateProgressBar() {
  const scrollTop = document.documentElement.scrollTop || document.body.scrollTop
  const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight
  scrollPercent.value = (scrollTop / windowHeight) * 100

  if (scrollPercent.value > moviestore.scrollThreshold) {
    moviestore.loadMoreMovies();
  }
}

const isSearch = computed(() => {
  if (searchWord.value) {
    return true
  } else {
    return false
  }
})

const searchMovie = function () {
  axios({
    method: 'get',
    url: `${moviestore.API_URL}/api/v1/movies/search/${searchWord.value}/`
  })
    .then(res => {
      movies.value = res.data
    })
    .catch(err => console.log(err))
}

watch(() => searchWord.value, () => {
  searchMovie()
})
</script>

<style scoped>
.align {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.genre-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
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

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.search {
  position: relative;
  width: 300px;
  margin-top: 50px;
}

.search-input {
  font-size: 15px;
  color: #222222;
  width: 300px;
  border: none;
  border-bottom: solid #aaaaaa 1px;
  padding-bottom: 10px;
  padding-left: 10px;
  position: relative;
  background: none;
  z-index: 5;
}

input::placeholder { color: #aaaaaa; }
input:focus { outline: none; }

span {
  display: block;
  position: absolute;
  bottom: 0;
  left: 50%;  /* right로만 바꿔주면 오 - 왼 */
  background-color: #666;
  width: 0;
  height: 2px;
  border-radius: 2px;
  transform: translateX(-50%);
  transition: 0.5s;
}

label {
position: absolute;
color: #aaa;
left: 50%;
transform: translateX(-50%);
font-size: 18px;
bottom: 8px;
transition: all .2s;
}

input:focus ~ label, input:valid ~ label {
font-size: 16px;
bottom: 40px;
}
</style>