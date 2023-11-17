<template>
  <div>
    <h1>Detail</h1>
    <div>
      <p>글 번호: {{ movie?.id }}</p>
      <img v-if="movie && movie.poster_path" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="#">
      <p>제목: {{ movie?.title }}</p>
      <p>내용: {{ movie?.overview }}</p>

    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';




const route = useRoute()
const store = useCounterStore()


const movie = ref(null)

onMounted(()=>{
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}`
  })
  .then((res)=>{
      console.log(res.data)
      movie.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
})
</script>

<style>

</style>
