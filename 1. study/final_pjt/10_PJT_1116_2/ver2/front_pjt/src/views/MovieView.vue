<template>
  <div>
    <h1>Movie Page</h1>
    <RouterLink :to="{name:'CreateView'}">[CREATE]
    </RouterLink>
    <MovieCard 
    v-for="movie in store.movies" 
    :key="movie.id" 
    :movie="movie" 
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'
import MovieCard from '@/components/MovieCard.vue';
const store = useCounterStore()

onMounted(()=>{
  store.getMovies()
})
</script>

<style>

</style>





