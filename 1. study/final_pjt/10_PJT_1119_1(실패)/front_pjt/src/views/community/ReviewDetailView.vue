<template>
  <div>
    <h1>Detail</h1>
    <div v-if="isEditing">
      <form @submit.prevent="reviewUpdate">
        <label for="title">제목:</label>
        <input v-model="title" id="title">
        <label for="content">내용:</label>
        <textarea v-model="content" id="content"></textarea>
        <button type="submit">수정 완료</button>
        <button @click="reviewDelete">삭제하기</button>
      </form>
    </div>
    <div v-else>
      <div v-if="review">
        <h5>{{ review.id }}</h5>
        <p>제목 : {{ review.title }}</p>
        <p>내용 : {{ review.content }}</p>
        <p>작성일 : {{ review.created_at }}</p>
        <p>수정일 : {{ review.updated_at }}</p>
        <button @click="toggleEditing">수정하기</button>
      </div>
    </div>
    <h3>Comment</h3>
    <CommentForm :review="review"/>
    <CommentList :review="review"/>
  </div>

</template>

<!-- 수정 시 기존 값 넣어두기 구현 추가 필요 -->

<!-- required 역할 : 비었을 시 제출 방지 -->

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommentForm from '@/components/community/CommentForm'
import CommentList from '@/components/community/CommentList'


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
// 이거 null로 해서 오류 뜨던데 이유가??
const review = ref({})

const title = ref('')
const content = ref('')
const isEditing = ref(false)

const toggleEditing = function () {
  isEditing.value = !isEditing.value
}

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/community/review/${route.params.id}/`
  })
    .then((res) => {
      console.log(res.data)
      review.value = res.data

    })
    .catch((err) => {
      console.log(err)
    })
})

const reviewUpdate = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/community/review/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {                                  //
      Authorization: `Token ${store.token}`     
    }
  })
    
    .then((res) => {
      console.log(res.data)
      router.push({name:'ReviewView'})
    })
    .catch((err) => {
      console.log(err)
    })
}

const reviewDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/community/review/${route.params.id}/`,
    headers: {                                  //
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      console.log(res.data)
      router.push({name:'ReviewView'})
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>
