<template>
  <div class="child">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
  defineProps({
    child : Object,
  })
</script>

<style scoped>
.child{
  border: 1px solid lightgray;
  margin: 10px;
  background-color: whitesmoke;
}
</style>