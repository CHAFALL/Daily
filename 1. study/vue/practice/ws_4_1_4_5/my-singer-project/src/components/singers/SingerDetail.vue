<template>
  <card class="singer-detail">
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg" alt="#" class="singer-image">
    <p>가수 소개글</p>
    <SingerAlbum />
    <SingerAlbum />
  </card>
</template>

<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue';


</script>

<style scoped>

.singer-detail{
  border: 1px solid black;
  text-align: center;
}

.singer-image{
  width: 200px;
  border-radius: 50%;
}

</style>