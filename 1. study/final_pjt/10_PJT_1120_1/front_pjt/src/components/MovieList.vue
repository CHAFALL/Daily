<!-- <template>
  <div class="movie-list-container">
    <h3>Movie List</h3>
   
    <div class="d-flex justify-space-between mb-6 bg-surface-variant">
      
      <MovieCard 
        v-for="movie in store.movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  
  </div>
</template> -->
<template>
  <hr>
  <div>
    dd{{ store.genres }}
  </div>
  <hr>
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

  <h3>당신만을 위해 뽑은 추천 영화 TOP 10 !!!</h3>
  <div class="carousel">
    <div class="d-flex justify-space-between mb-6 bg-surface-variant ">
      <MovieCard
        v-for="(movie, index) in rnakList.slice(0, 10)"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>

  <h3 @click="goGenre">장르별</h3>
  <div class="carousel">
    <div class="d-flex justify-space-between mb-6 bg-surface-variant ">
      <MovieCard
        v-for="(movie, index) in rnakList.slice(0, 10)"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
  


  
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted } from 'vue'
import MovieCard from './MovieCard.vue';
const store = useCounterStore()

const rnakList = ref([])

// 정렬 함수
const sortByVoteAvg = (a, b) => b.vote_avg - a.vote_avg;

// const goGenre = function () {

// }

// 컴포넌트가 마운트될 때 호출
onMounted(() => {
  // vote_avg를 기준으로 정렬
  rnakList.value = [...store.movies].sort(sortByVoteAvg);
});
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