<template>
  <div>
    <h3>Review List</h3>
    <ReviewListItem 
      v-for="review in store.reviews"
      :key="review.id"
      :review="review"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ReviewListItem from '@/components/ReviewListItem.vue'

const store = useCounterStore()
console.log(store.reviews)
</script>
