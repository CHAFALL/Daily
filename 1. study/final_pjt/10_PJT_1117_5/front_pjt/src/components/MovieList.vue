
<template>
  <h3>Movie List</h3>
  <div class="carousel">
   
    <div class="d-flex justify-space-between mb-6 bg-surface-variant ">
      
      <MovieCard 
        v-for="movie in store.movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import MovieCard from './MovieCard.vue';
const store = useCounterStore()
</script>

<style scoped>

.carousel{
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: thin; /* Firefox에서 스크롤 바 크기 조절 */
  scrollbar-color: gray transparent; /* Firefox에서 스크롤 바 색상 조절 */
}
</style>
