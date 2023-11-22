<template>
  <br><br><br>
  <v-app style="background-color: #333;">
    <v-container fluid fill-height>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="10" md="8" lg="6">
          <v-card class="elevation-12" style="border-radius: 10px; text-align: center; padding: 20px; color: #000;">
            <v-card-title class="text-h3">
              Article Page
            </v-card-title>
            <v-btn @click="goToReviewCreateView" dark style="margin: 10px;">
              게시글 작성
            </v-btn>
            <ReviewList />
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ReviewList from '@/components/community/ReviewList.vue'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()

onMounted(() => {
  store.getReviews()
})

const goToReviewCreateView = () => {
  router.push({ name: 'ReviewCreateView' })
}
</script>

<style>
</style>