<template>
  <div class="center">
    <h1>App.vue</h1>
    <MainPage/>
    <SingerList/>
  </div>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';
import SingerList from '@/components/singerList.vue';



</script>

<style scoped>
.center {
  text-align: center;
}
</style>