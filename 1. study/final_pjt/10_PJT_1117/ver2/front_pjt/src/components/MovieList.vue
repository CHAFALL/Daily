<template>
  <div>
    <h3>movie List</h3>
    <MovieCard 
    v-for="movie in store.movies"
    :key="movie.id"
    :movie="movie"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import MovieCard from './MovieCard.vue';
const store = useCounterStore()
</script>
