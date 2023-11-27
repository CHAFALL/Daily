<template>

  <br><br><br><br><br><br>
  <div class="back">
  <h3 class="white-text">찜한 영화 목록</h3>
    <div class="carousel" >
    
      <div class="d-flex justify-space-between mb-6 bg-surface-variant" >
        <!-- {{ store.userInfo }} -->
        <MovieCard 
          v-for="movie in filteredMovies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
  </div>

  
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted, computed } from 'vue';
import MovieCard from '@/components/MovieCard.vue';

const store = useCounterStore();


const userId = store.userInfo.user_info.id;


onMounted(()=>{
  store.getMovies()
})


const filteredMovies = computed(() => {
  return store.movies.filter((movie) => { 
    return movie.like_users.some((user) => user === userId);
  });
});


</script>

<style>

.carousel{
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: thin; /* Firefox에서 스크롤 바 크기 조절 */
  scrollbar-color: gray transparent; /* Firefox에서 스크롤 바 색상 조절 */
}

.white-text {
  color: white;
  font-size: 25px;
}
/* 스크롤 바의 색상을 설정합니다. */
/* Chrome, Safari, Edge */
.carousel::-webkit-scrollbar {
  width: 12px;
}

.carousel::-webkit-scrollbar-thumb {
  background-color: #7a7a7a; /* 스크롤 바의 색상 */
}

</style>