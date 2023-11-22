<template>
  <div>
    <h1>Movie Page</h1>
    <MovieList />
  </div>
</template>

<script setup>
import MovieList from '@/components/MovieList.vue'
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

onMounted(()=>{
  store.getMovies()
  store.getGenre()
  store.getUserInfo()
})





</script>

<style scoped>

</style>
