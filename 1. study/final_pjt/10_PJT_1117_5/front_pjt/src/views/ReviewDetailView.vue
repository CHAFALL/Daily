<template>
  <div>
    <h1>Detail</h1>
    <div v-if="review">
      <p>제목 : {{ review.title }}</p>
      <p>내용 : {{ review.content }}</p>
      <p>작성일 : {{ review.created_at }}</p>
      <p>수정일 : {{ review.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const review = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/community/review/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      review.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style>

</style>
