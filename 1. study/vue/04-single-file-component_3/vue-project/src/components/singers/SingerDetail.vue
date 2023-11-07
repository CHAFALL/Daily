<template>
  <div class='card'>
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg" alt="#">
    <p>가수 소개글</p>
    <SingerAlbum/>
  </div>
</template>

<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue';


</script>

<style scoped>

  .card{
    border : 1px solid;
    display : inline-block;
    width : 40%;
    margin: 20px;
  }


  img{
    width : 200px;
    border-radius: 50%;
  }
</style>
