<template>
  <div>
    <h5>댓글 작성</h5>
    <form @submit.prevent="createComment">
      <div>
        <label for="content">내용:</label>
        <input type="text" id="content" v-model.trim="content" >
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const props = defineProps({
  review: Object,
})

const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createComment = function () {
  
  axios({
    method: 'post',
    url: `${store.API_URL}/community/reviews/${props.review.id}/comments/`,
    data: {
      content: content.value
    },
    headers: {                                  //
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      console.log(res)
      // 이거 왜 해준거지???
      router.push({ name: 'ReviewDetailView' })
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>
