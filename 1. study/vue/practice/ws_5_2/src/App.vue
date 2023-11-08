<template>
  <div class="container">
    <header>
      <h1>명함 관리 페이지</h1>
    </header>
      <main>
        <article>
          <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
        </article>
      </main>
    <footer>
      ⓒ 2023 My Business Cards
    </footer>
  </div>
</template>

<script setup>

</script>

<style scoped>

.container{
  text-align: center;
}
header{
  text-align: center;
  border : 1px solid white;
  background-color: rgb(105, 186, 212);
  display: inline-block;
  width: 30%;
  color: white;
}

footer{
  border : 1px solid;
  background-color: rgb(243, 238, 238);
  padding-top: 20px;
  position: fixed;
  bottom: 0;
  width: 100%;

}
</style>