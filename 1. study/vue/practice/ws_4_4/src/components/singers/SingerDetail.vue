<template>
  <div>
    <div class='singer'>
      <h1>가수 이름</h1>
      <img src="@/assets/singer.jpg" alt="#" >
      <p>가수 소개글</p>
    </div>
    <div class='singer'>
      <h1>가수 이름</h1>
      <img src="@/assets/singer.jpg" alt="#" >
      <p>가수 소개글</p>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>

  .singer {
    border: 0.5px solid black;
    display: inline-block;
    width : 40%;
    margin: 20px;
  }

  img {
    width: 200px;
    border-radius: 50%;
  }
</style>