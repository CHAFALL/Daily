<template>
  <div class="img-container">
    <p>Meow</p>
  </div>
</template>

<script setup>

</script>

<style scoped>
  .img-container{
    margin-top: 0px;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    font-size: 200px;
    color: white;
    width: 100vw;
    height: 100vh;

    background-image:  linear-gradient(rgba(0, 0, 0, 0.5), rgba(252, 249, 249, 0.2)),
  url('@/assets/부추1.jpg');
  }

  p{
    margin-top: 0px;
  }
</style>
