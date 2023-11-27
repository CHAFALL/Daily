<template>
  <div>
    <h3 >게시글 리스트</h3>
    <hr>
    <ReviewListItem 
      v-for="review in store.reviews"
      :key="review.id"
      :review="review"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ReviewListItem from '@/components/community/ReviewListItem.vue'

const store = useCounterStore()
</script>
