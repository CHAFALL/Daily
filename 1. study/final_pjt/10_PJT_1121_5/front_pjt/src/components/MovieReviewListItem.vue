<template>
  <div v-if="comment && comment.content" class="comment-container">
    
    <span class="user-name">{{ comment.user_name }}</span> - 
    <span class="comment-content">{{ comment.content }}</span> -
    <v-rating v-model="comment.rank" :readonly="true" class="star-rating"></v-rating>
  
  </div>
</template>

<script setup>
const props = defineProps({
  comment: Object
});
</script>

<style lang="scss" scoped>
.comment-container {
  color: green;
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