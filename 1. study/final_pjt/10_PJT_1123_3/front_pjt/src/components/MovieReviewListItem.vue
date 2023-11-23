<template>
  <div v-if="comment && comment.content" class="comment-container">
    
    <span class="user-name">{{ comment.user_name }}</span> - 
    <span class="comment-content">{{ comment.content }}</span>
    <span> ({{ comment.rank }}점) </span>
    
   
    
    <v-btn 
    @click="commentDelete()" 
    v-if="comment.user_name == store.userInfo.user_info.username"
    style="margin-left: 10px; background: #333; color: #ccc; block-size: 25px; font-family: 'Your Font Name', sans-serif;"
    > 
    삭제 
    </v-btn>
  

    <!-- <v-rating v-model="comment.rank" :readonly="true" class="star-rating"></v-rating> -->
  
  </div>
</template>

<script setup>
import router from '@/router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore()

const props = defineProps({
  comment: Object
});

const commentDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/movie_reviews/${props.comment.id}/`,
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

<style lang="scss" scoped>
.comment-container {
  color: rgb(170, 165, 165);
  margin-bottom: 10px;
  padding: 10px;

  .user-name {
    font-weight: bold;
    margin-right: 5px;
  }

  .comment-content {
    margin-right: 5px;
  }

  .star-rating {
    color: #ff9800; // Set the star color
  }
}
</style>