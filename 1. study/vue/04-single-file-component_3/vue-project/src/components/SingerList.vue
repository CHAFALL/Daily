<template>
  <div>
    <h1>가수 목록</h1>
    <SingerDetail v-for="singer in singers"/>
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';
// 이거 빼먹지 말기!!
import {ref} from 'vue'

const singers = ref([
  {name : 'adele'},
  {name : 'maroon5'},
  {name : 'Dua Lipa'},
])

</script>

<style scoped>
  h1{
    color: orangered;
  }
</style>