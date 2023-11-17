<template>
  <div>
    <h1>Movie Page</h1>
    <RouterLink :to="{name:'CreateView'}">[CREATE]
    </RouterLink>
    <MovieList />
  </div>
</template>

<script setup>
import MovieList from '@/components/MovieList.vue'
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'
const store = useCounterStore()

onMounted(()=>{
  store.getMovies()
})
</script>

<style>

</style>
