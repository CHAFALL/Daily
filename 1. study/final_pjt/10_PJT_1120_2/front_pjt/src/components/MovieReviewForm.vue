<template>
  <div>
    <h5>리뷰 작성</h5>
    <form @submit.prevent="createComment" style="color: green;">
      <div>
        <label for="content">내용:</label>
        <v-text-field v-model="content" id="content"></v-text-field>
      </div>

      <div>
        <v-rating v-model="rank" :max="5" :min="0" :precision="1"></v-rating>
      </div>
      <v-btn  variant="outlined" type="submit" value="제출">
        제출
      </v-btn>

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
    headers: {                                  
      Authorization: `Token ${store.token}`     
    }
  })
    .then((res) => {
      console.log(res)
      // router.push({ name: 'DetailView' })
      router.go(0)
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>
