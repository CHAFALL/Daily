<template>
  <div>
    <button @click="createArticle">게시글 생성</button>
    <div v-for="article in store.articles">
      <h4>{{ article.id }}번 게시글</h4>
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.content }}</p>
      <hr>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router'
const store = useArticleStore()
const router = useRouter()
onMounted(() => {
  store.getArticles()
})

const createArticle = function () {
  router.push({name : 'create'})
}
</script>

<style scoped>

</style>