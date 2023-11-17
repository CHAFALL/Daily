<template>
  <div>
    <h5>{{ review.id }}</h5>
    <p>{{ review.title }}</p>
    <p>{{ review.content }}</p>
    <RouterLink :to="{ name: 'ReviewDetailView', params: { id: review.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>

defineProps({
  review: Object
})
</script>
