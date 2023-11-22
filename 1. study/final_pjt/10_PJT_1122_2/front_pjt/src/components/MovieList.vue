
<template>


  <div class="back">
  <h3 class="white-text">Movie List</h3>
  
  <!-- 장르별 -->
  <h3 class="white-text"> 모험 장르 뽑기</h3>
  <button style="color: aqua;" @click="getRandom">당신이 좋아하는 장르순으로 랜덤 추천 해드립니다.</button>
  <div class="carousel">
    <div class="d-flex justify-space-between mb-6 bg-surface-variant ">
      <MovieCard 
        :movie="choiceMovie"
      />
    </div>
  </div>
  
  
  <div class="carousel" >
    <div class="d-flex justify-space-between mb-6 bg-surface-variant" >
      <MovieCard 
        v-for="movie in store.movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
<br><br><br><br>
<!-- 평점 탑 텐 -->
  <h3 class="white-text">당신만을 위해 뽑은 추천 영화 TOP 10 !!!</h3>
  <div class="carousel">
    <div class="d-flex justify-space-between mb-6 bg-surface-variant ">
      <MovieCard
        v-for="(movie, index) in rankList.slice(0, 10)"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>

<br><br><br><br>
  
</div>


  
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted, computed } from 'vue'
import MovieCard from './MovieCard.vue';

const store = useCounterStore()

const rankList = ref([])

const choiceMovie = ref([])



// 정렬 함수
const sortByVoteAvg = (a, b) => b.vote_avg - a.vote_avg;

// 컴포넌트가 마운트될 때 호출
onMounted(() => {
  // vote_avg를 기준으로 정렬
  rankList.value = [...store.movies].sort(sortByVoteAvg);
  getRandom()
});

// 가중치를 활용한 랜덤 초이스
const getRandom = () => {
  store.getUserInfo()
  for (const movie of store.movies) {
    // console.log('영화', movie.title);

    // movie.genres 배열에 store.userInfo.randomChoice가 포함되어 있는지 확인
    if (movie.title === store.userInfo.pick_movie) {
      choiceMovie.value = movie
    }
  }
};


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