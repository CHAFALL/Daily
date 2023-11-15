<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="onSubmit">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title">
      <label for="content">내용: </label>
      <input type="text" id="content" v-model.trim="content">
      <input type="submit">
    </form>
    
  </div>

</template>

<script setup>
  import {ref} from 'vue'
  import {useArticleStore} from '@/store/articles'

  store = useArticleStore()

  const title = ref('')
  const content = ref('')

  const onSubmit = function () {
    const payload = {
      title: title.value,
      content: content.value,
    }
    store.createArticles(payload)
  }
</script>

<style scoped>

</style>