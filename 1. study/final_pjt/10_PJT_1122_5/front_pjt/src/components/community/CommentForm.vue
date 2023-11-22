<template>
  <div>
    <v-form @submit.prevent="createComment">
      <v-row>
        <v-col cols="12">
          <v-text-field v-model.trim="content" label="내용"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-btn type="submit" color="grey darken-2">작성</v-btn>
        </v-col>
      </v-row>
    </v-form>
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
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'ReviewDetailView' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
/* Add any additional styling here */
</style>