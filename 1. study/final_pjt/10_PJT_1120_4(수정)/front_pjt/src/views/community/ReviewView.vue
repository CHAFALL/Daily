<template>
  <div>
    <h1>Review Page</h1>
    <RouterLink :to="{ name: 'ReviewCreateView' }">
      [CREATE]
    </RouterLink>
    <ReviewList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ReviewList from '@/components/community/ReviewList.vue'
import { RouterLink } from 'vue-router'

const store = useCounterStore()

onMounted(() => {
  store.getReviews()
})

</script>

<style>

</style>
