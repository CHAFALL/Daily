<template>
  <div class="img-content">
    <img :src="imgUrl+movie.poster_path" alt="" @click="router.push({name: 'movie', params:{id: movie.id}})">
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
  movie: Object
})

const imgUrl = 'https://image.tmdb.org/t/p/w185'
</script>

<style scoped>
  .img-content {
    cursor: pointer;
  }
</style>