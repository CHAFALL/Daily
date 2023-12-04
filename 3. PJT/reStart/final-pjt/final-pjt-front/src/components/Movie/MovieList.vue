<template>
  <div class="card-container">
    <template v-if="movies && movies.length > 0">
      <MovieListItem
        class="card"
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </template>
    <div v-else>
      해당 조건을 만족하는 영화가 없습니다.
    </div>
  </div>
</template>

<script setup>
import MovieListItem from '@/components/Movie/MovieListItem.vue'
import { useMovieStore } from '@/stores/movies'
const moviestore = useMovieStore()
const props = defineProps({
  movies: Object
})

</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  text-align: center;
}

.card:hover {
  transform: scale(1.05);
  transition: transform 0.5s ease;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}

.card {
  width: 250px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin: 5px;
  padding: 10px;
  box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  background-color: rgb(226, 226, 226);
  transition: box-shadow 0.5s ease;
}

.card img {
  width: 100%;
  height: auto;
}

</style>
