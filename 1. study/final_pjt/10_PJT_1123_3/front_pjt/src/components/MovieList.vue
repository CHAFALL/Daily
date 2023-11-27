
<template>


  <div class="back" style="margin: 100px;">
  
  <!-- 추천 알고리즘 -->
  <div class="carousel">
    <div 
    style="height: 410px;"
    class="d-flex justify-space-between mb-6 bg-surface-variant" >
      <MovieCard2 
    
      :movie="choiceMovie"
      />
    </div>
    <div style="width: 1200px; margin-left: 100px; ">
      <h3 style="color: #ff9800"> 평점 </h3>
      <hr>
      <h4 style="color: aliceblue">{{ choiceMovie?.vote_avg }}</h4>
      <br>
      <h5 style="color: #ff9800;">줄거리</h5>
      <hr>
      <p v-if="choiceMovie.overview" class="movie-overview">{{ choiceMovie.overview }}</p>
      <p v-else class="movie-overview">줄거리가 없습니다.</p>
    </div>
  </div>
  <p style="color: white;">너만을 위한 영화추천↓</p>
  <v-btn style="color: black; left: 145px;" @click="getRandom">클릭</v-btn>
  <br>
  <br>
  <!-- 장르별 -->
  
      <button style="color: white;" @click="filterGenre(12)">모험</button> //
      <button style="color: white;" @click="filterGenre(14)">판타지</button> //
      <button style="color: white;" @click="filterGenre(16)">애니메이션</button> //
      <button style="color: white;" @click="filterGenre(18)">드라마</button> //
      <button style="color: white;" @click="filterGenre(27)">공포</button> //
      <button style="color: white;" @click="filterGenre(28)">액션</button> //
      <button style="color: white;" @click="filterGenre(35)">코미디</button> //
      <button style="color: white;" @click="filterGenre(36)">역사</button> //
      <button style="color: white;" @click="filterGenre(37)">서부</button> //
      <button style="color: white;" @click="filterGenre(53)">스릴러</button> //
      <button style="color: white;" @click="filterGenre(80)">범죄</button> //
      <button style="color: white;" @click="filterGenre(99)">다큐멘터리</button> //
      <button style="color: white;" @click="filterGenre(878)">SF</button> //
      <button style="color: white;" @click="filterGenre(9648)">미스터리</button> //
      <button style="color: white;" @click="filterGenre(10402)">음악</button> //
      <button style="color: white;" @click="filterGenre(10749)">로맨스</button> //
      <button style="color: white;" @click="filterGenre(10751)">가족</button> //
      <button style="color: white;" @click="filterGenre(10752)">전쟁</button> //
      <button style="color: white;" @click="filterGenre(10770)">TV 영화</button> //
      
      <div class="carousel" >
    <div class="d-flex justify-space-between mb-6 bg-surface-variant" style="background-color: black;">
      <MovieCard  
        v-for="movie in genrePermovies"
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
  <!-- 전체 영화 정보 -->
  <h3 class="white-text">전체 영화 리스트</h3>
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
  
</div>


  
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted, computed } from 'vue'
import MovieCard from './MovieCard.vue';
import MovieCard2 from './MovieCard2.vue';


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


// 장르별
const genrePermovies = ref([])

const filterGenre = (genreId) => {
  const sample = ref([])
  for (const movie of store.movies) {
    if (movie.genres.includes(genreId)) {
      sample.value.push(movie)
      genrePermovies.value = sample.value
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



.movie-overview {
  
  font-size: 18px; /* 원하는 글씨 크기 설정 */
  color: #6C757D; /* 원하는 글씨 색상 설정 */
}


</style>