<template>
  <div>

    <h5>리뷰 작성</h5>
    <form @submit.prevent="createComment">
      <div>
        <label for="content">내용:</label>
        <input type="text" id="content" v-model.trim="content" >
      </div>
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

const props = defineProps({
  movie: Object,
})


const content = ref(null)
const rank = ref(0)
const store = useCounterStore()
const router = useRouter()

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/movies/${props.movie.id}/movie_reviews/`,
    data: {
      content: content.value,
      rank: rank.value, 
    },
    headers: {                                  //
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      console.log(res)
      // router.push({ name: 'DetailView',params:{id:props.movie.id} })
      router.go(0)
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>
