<template>
  <div class="accordion">
    <div class="accordion-item">
      <div class="accordion-title" @click="showLikedMovies = !showLikedMovies">
        <h2>{{user.username}}'s Prefered Movies</h2>
      </div>
      <transition name="slide-fade" appear>
        <div v-if="showLikedMovies" class="accordion-detail">
          <div class="carousel-container" v-if="movies && movies.length > 0">
            <div class="carousel">
            <UserLikeMovieItem
              v-for="movie in movies"
              :key="movie.id"
              :movie="movie"
            />
            </div>
          </div>
          <div v-else>
            <p>좋아요 한 영화가 없습니다.</p>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import UserLikeMovieItem from '@/components/User/UserLikeMovieItem.vue'
import { ref, onMounted, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
const userStore = useUserStore()
const props = defineProps({
  user: Object,
})
const movies = ref(null)
const showLikedMovies = ref(false) // showLikedMovies 변수 정의 및 초기값 설정

const fetchData = async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `${userStore.API_URL}/api/v1/movies/${props.user.username}/like/movies/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    movies.value = response.data
  } catch (error) {
    console.log(error)
  }
}

onMounted(fetchData)

watch(() => props.user, () => {
  fetchData()
})

</script>

<style scoped>
.accordion {
  width: 80%;
  margin: 0 auto;
  font-family: 'Noto Sans KR', sans-serif;
  transition: 1ms;
}

.accordion-item {
  background: #282828;
  margin-bottom: .5rem;
  box-shadow: 0 .1rem 1rem -.5rem rgba(0,0,0,.4);
  border-radius: 5px;
  overflow: hidden;
}

.accordion-title{
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  background: #333;
  cursor: pointer;
  position: relative;
  height: 50px;
  font-family: 'Indie Flower', cursive;
  color: #fff;
}

.accordion-detail {
  padding: 1rem;
  background-color: #444;
  color: #fff;
}

.carousel-container {
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: thin;
  scrollbar-color: #888 transparent;
}

.carousel::-webkit-scrollbar {
  width: 8px;
}

.carousel::-webkit-scrollbar-track {
  background-color: transparent;
}

.carousel::-webkit-scrollbar-thumb {
  background-color: #888;
  border-radius: 4px;
}

.carousel::-webkit-scrollbar-thumb:hover {
  background-color: #555;
}

.carousel {
  display: flex;
  gap: 16px;
  padding-bottom: 16px;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: max-height .6s ease, opacity .5s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  max-height: 0;
  opacity: 0;
}

.slide-fade-enter-to,
.slide-fade-leave-from {
  max-height: 100vh;
  opacity: 1;
}
</style>
