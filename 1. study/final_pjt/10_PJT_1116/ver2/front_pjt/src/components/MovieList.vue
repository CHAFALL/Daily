<template>
  <div>
    <h3>movie List</h3>
    <MovieListItem 
    v-for="movie in store.movies"
    :key="movie.id"
    :movie="movie"
    />
  </div>
</template>

<script setup>
import MovieListItem from '@/components/MovieListItem.vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
</script>
