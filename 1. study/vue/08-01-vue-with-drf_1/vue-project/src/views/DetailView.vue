<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.content }}</p>
      <p>작성일: {{ article.created_at }}</p>
      <p>수정일: {{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router';

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
//null 문제 해결법: ?.로 해결하거나 v-if로 해결하기!(실제로 있을 때만 출력하도록)

onMounted(()=>{
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res)=>{
      console.log(res.data)
      article.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
})
</script>

<style>

</style>
