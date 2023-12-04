<template>
  <div v-if="actor" class="container">
    <div class="actor-container">
      <h1>{{ actor.name }}</h1>
      <img :src="imgUrl + actor.profile_path" alt="">
      <!-- <p>{{ actor }}</p> -->
      <h3>출연작</h3>
      <MovieList :movies="movies"/>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import MovieList from '@/components/Movie/MovieList.vue'
const userStore = useUserStore()
const route = useRoute()

const actor = ref(null)
const movies = ref(null)
const imgUrl = "https://image.tmdb.org/t/p/h632"
// w45 / w185 / h632 / original

const fetchActorData = function () {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/movies/actor/${route.params.id}/`,
  })
    .then(res => {
      actor.value = res.data.actor
      movies.value = res.data.movies
    })
    .catch(err => console.log(err))
}

onMounted(() => {
  fetchActorData()
})

</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  /* height: 100vh; */
  margin-top: 80px;
  z-index: 1;
}

.actor-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 1px solid lightgrey;
  border-radius: 20px;
  width: 700px;
  height: auto;
  text-align: center;
  margin-bottom: 50px;
}
</style>