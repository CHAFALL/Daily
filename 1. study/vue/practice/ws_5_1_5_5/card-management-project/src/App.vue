<template>
  <div class="app">
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
      <main class="main">
        <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>  
      </main>
      <article class="article">
        <!-- 나중에 컴포넌트 등록 -->
        <CreateCardForm
          @create-card-event="updateCard"
        />
        <BusinessCard
          :new-card="newCard"
        />
      </article>
    <footer class="footer">
      <p>&copy; 2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>
  import BusinessCard from '@/components/BusinessCard.vue';
  import CreateCardForm from '@/components/CreateCardForm.vue';
  import {ref} from 'vue'

  const newCard = ref({})

  const updateCard = function (cardInfo) {
    newCard.value = cardInfo
  }

</script>

<style scoped>
  .app {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    text-align: center;
  }
  .header{
    background-color: rgb(108, 108, 236);
    color: white;
    padding: 20px;
  }

  .main{
    
    padding: 20px;
  }

  .article{
    padding: 20px;
    flex-grow: 1;
  }

  .footer{
    background-color: lightgray;
    width: 100%;
  }
</style>