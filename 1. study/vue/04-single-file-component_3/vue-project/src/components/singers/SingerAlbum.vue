<template>
  <div class="card2">
    <h5> 앨범 제목 </h5>
    <ul> 
      <li> 노래 목록1</li>
      <li> 노래 목록2</li>
      <li> 노래 목록3</li>
    </ul>
  </div>
  <div class="card2">
    <h5> 앨범 제목 </h5>
    <ul> 
      <li> 노래 목록1</li>
      <li> 노래 목록2</li>
      <li> 노래 목록3</li>
    </ul>
  </div>
</template>

<script setup>

</script>

<style scoped>
  ul{
    list-style: none;
    padding-left: 0px;
    color: orange;
  }

  .card2{
    border: 1px solid lightgray;
    width: 30%;
    background-color: whitesmoke;
    border-radius: 10%;
    /* 밑에것만 하면 텍스트 느낌으로 되는건가? */
    display: inline-block;
    margin: 20px;
  }
</style>