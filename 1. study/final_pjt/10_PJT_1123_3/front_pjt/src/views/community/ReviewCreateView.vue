<template>
  <br><br><br>
  <v-container fluid fill-height style="background-color: #333; color: white; padding: 20px;">
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="elevation-12" style="border-radius: 10px; text-align: center; padding: 20px;">
          <v-card-title class="text-h3">
            게시글 작성
          </v-card-title>
          <form @submit.prevent="createReview">
            <v-row>
              <v-col cols="12">
                <v-text-field v-model.trim="title" label="제목" outlined></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-textarea v-model.trim="content" label="내용" outlined></v-textarea>
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
            <v-row style="margin-top: 10px;">
              <v-col>
                <v-btn type="submit" dark color="grey darken-2">작성</v-btn>
              </v-col>
              <v-col>
                <v-btn @click="cancel" dark color="grey darken-2">취소</v-btn>
              </v-col>
            </v-row>
          </form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const title = ref(null);
const content = ref(null);
const movieTitle = ref('');
const rank = ref(0);
const store = useCounterStore();
const router = useRouter();

const createReview = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/community/review/`,
    data: {
      title: title.value,
      content: content.value,
      movie_title: movieTitle.value,
      rank: rank.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.push({ name: 'ReviewView' });
    })
    .catch((err) => {
      console.log(err);
    });
};

const cancel = function() {
  router.push({ name: 'ReviewView' })
}
</script>

<style scoped>
/* Add any additional styling here */
</style>