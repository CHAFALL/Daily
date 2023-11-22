<template>
  <br><br>
  <div style="color: white;">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createReview">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
        <label for="movieTitle">영화 제목:</label>
        <input v-model="movieTitle" id="movieTitle">
        <label for="rank">평점:</label>
        <input v-model="rank" id="rank" type="number" min="0" max="10">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const movieTitle = ref('')
const rank = ref(0)
const store = useCounterStore()
const router = useRouter()

const createReview = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/community/review/`,
    data: {
      title: title.value,
      content: content.value,
      movie_title: movieTitle.value,
      rank: rank.value, 
    },
    headers: {                                  //
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'ReviewView' })
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>
