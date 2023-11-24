<template>
  <div style="margin-top: 20px;" v-if="comment && comment.content">
    <span>{{ comment.user_name }}</span> - <span>{{ comment.content }}</span>
    <v-btn 
    @click="commentDelete()" 
    v-if="comment.user_name == store.userInfo.user_info.username"
    style="margin-left: 10px; background: #333; color: #ccc; block-size: 25px; font-family: 'Your Font Name', sans-serif;"
    > 
    삭제 
    </v-btn>
  </div>





</template>

<script setup>
import router from '@/router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore()


const props = defineProps({
  comment: Object
})

const commentDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/community/comments/${props.comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.go(0)
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style scoped>

</style>

