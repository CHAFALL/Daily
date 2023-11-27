<template>
  <br><br><br>
  <v-container fluid fill-height style="background-color: #333; color: white; padding: 20px;">
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="elevation-12" style="border-radius: 10px; text-align: center; padding: 20px;">
          <v-card-title class="text-h3">
            Detail
          </v-card-title>
          <v-row v-if="isEditing">
    <v-col cols="12">
      <v-form @submit.prevent="reviewUpdate">
        <v-row>
          <v-col cols="12">
            <v-text-field v-model="title" label="제목" outlined>
              
            </v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-textarea v-model="content" label="내용" outlined></v-textarea>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field v-model="movieTitle" label="영화 제목" outlined></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field v-model="rank" label="평점" type="number" min="0" max="10" outlined></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-btn type="submit" style="margin-right: 60px;">수정 완료</v-btn>
            <v-btn @click="reviewDelete" style="margin-left: 60px;">삭제하기</v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-col>
  </v-row>
          <v-row v-else>
            <v-col cols="12">
              <v-row v-if="review">
                <v-col cols="12">
                  <h5>{{ review.id }}</h5>
                  <p>{{ review.user_name }}</p>
                  <span>영화제목:{{ review.movie_title }}</span> - <span>{{ review.rank }}점</span>
                  <p>제목 : {{ review.title }}</p>
                  <p>내용 : {{ review.content }}</p>
                  <p>작성일 : {{ formatDate(review.created_at) }}</p>
                  <p>수정일 : {{ formatDate(review.updated_at) }}</p>
                  <v-btn @click="toggleEditing">수정하기</v-btn>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <h3>Comment</h3>
              <CommentForm :review="review" />
              <CommentList :review="review" />
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

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
const review = ref({})
const title = ref('')
const content = ref('')
const movieTitle = ref('')
const rank = ref(0)
const isEditing = ref(false)

const toggleEditing = function () {
    title.value = review.value.title;
    content.value = review.value.content;
    movieTitle.value = review.value.movie_title;
    rank.value = review.value.rank;
    console.log('확인용',review.value)
  
  isEditing.value = !isEditing.value;
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
      content: content.value,
      movie_title: movieTitle.value,
      rank: rank.value, 
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({name: 'ReviewView'})
    })
    .catch((err) => {
      console.log(err)
    })
}

const reviewDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/community/review/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({name: 'ReviewView'})
    })
    .catch((err) => {
      console.log(err)
    })
}


const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  });
};


</script>

<style scoped>
/* Add any additional styling here */
</style>