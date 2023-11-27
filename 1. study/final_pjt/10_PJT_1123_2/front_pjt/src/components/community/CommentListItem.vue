<template>
  <div v-if="comment && comment.content">
    <span>{{ comment.user_name }}</span> - <span>{{ comment.content }}</span>
  </div>

</template>

<script setup>

defineProps({
  comment: Object
})

</script>

<style lang="scss" scoped>

</style>

