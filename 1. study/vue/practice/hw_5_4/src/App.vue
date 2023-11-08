<template>
  <div class="card">
    <ParentPage />
  </div>
</template>


<script setup>
  import ParentPage from '@/components/ParentPage.vue';
  </script>

<style scoped>

.card{
  border : 1px solid lightgray;
  margin : 10px;
}

div {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}
h3 {
  font-size: 18px;
}
p {
  font-size: 14px;
}
</style>
