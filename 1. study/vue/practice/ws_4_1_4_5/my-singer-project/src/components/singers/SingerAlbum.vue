<template>
  <div class="album">
    <div class="album-title">앨범제목</div>
    <ul class="song-list">
      <li class="song">노래 제목1</li>
      <li class="song">노래 제목2</li>
      <li class="song">노래 제목3</li>
    </ul>
  </div>
</template>

<script setup>

</script>

<style scoped>



  .album{
    display: inline-block;
    text-align: center;
    border: 1px solid lightgray;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    background-color: whitesmoke;
    box-shadow: 2px 2px 4px gray;
  }

  .song-list{
   list-style: none;
   padding: 0px; 
  }

  .album-title{
    font-weight: bold;
  }

  .song{
    color : orangered;
  }

</style>