<template>
  <div class="card">
    <h3>자식 페이지 입니다.</h3>
    <p>이름: {{ childName }}</p>
    <p>나이: {{ childAge }}</p>
  </div>
</template>

<script setup>
  defineProps({
    childName : String,
    childAge : Number,
  })
</script>

<style scoped>
.card{
  border : 1px solid lightgray;
  margin : 10px;
}
</style>