<template>
  <div>
    <h1>리뷰 작성</h1>
    <form @submit.prevent="createReview">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title">
      <label for="content">내용</label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
// import { useRouter } from 'vue-router';
const store = useCounterStore()
// const router = useRouter()

const title = ref('')
const content = ref('')

const createReview = function(){
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/review/`,
    // 여기서 왜 data인가?? axios로 확인해보면 암!
    data: {
      title: title.value,
      content:content.value,
    }
  })
    .then((res)=>{
      //console.log(res.data)
      // router.push({name:'MovieView'})
    })
    .catch((err)=>{
      console.log(err)
    })
  
}

</script>

<style>

</style>
