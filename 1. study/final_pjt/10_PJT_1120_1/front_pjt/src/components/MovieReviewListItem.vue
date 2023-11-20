<template>
  <div v-if="comment && comment.content">
    <span>{{ comment.user_name }}</span> - 
    <span>{{ comment.content }}</span> -
    <span>{{ comment.rank }}</span>
  </div>
</template>

<script setup>

const props = defineProps({
  comment: Object
})



</script>

<style lang="scss" scoped>

</style>

