<template>
  <div>
    <div v-if="loading">
      <p>Loading...</p>
    </div>
    <div v-else-if="hasArticles">
      <ArticleListItem
        v-for="(article, index) in paginatedArticles"
        :key="article.id"
        :article="article"
        :index="index"
      />
      <div class="pagination">
        <button @click="changePage(page - 1)" class="next-prev" :disabled="page === 1">Prev</button>
        <span>Page {{ page }} of {{ totalPages }}</span>
        <button @click="changePage(page + 1)" class="next-prev" :disabled="page === totalPages">Next</button>
      </div>
    </div>
    <div v-else>
      <p class="inner-text">게시글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/Article/ArticleListItem.vue'
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted, computed } from 'vue'

const articleStore = useArticleStore()
const page = ref(1)
const pageSize = 8
const loading = ref(true)

onMounted(async () => {
  await articleStore.getArticles() 
  loading.value = false
})

const hasArticles = computed(() => {
  return articleStore.articles && articleStore.articles.length > 0
})

const paginatedArticles = computed(() => {
  if (hasArticles.value) {
    const start = (page.value - 1) * pageSize
    const end = start + pageSize
    return articleStore.articles.slice(start, end)
  }
  return []
})

const totalPages = computed(() => {
  if (hasArticles.value) {
    return Math.ceil(articleStore.articles.length / pageSize)
  }
  return 1
})

const changePage = (newPage) => {
  if (newPage >= 1 && newPage <= totalPages.value) {
    page.value = newPage
  }
}
</script>

<style scoped>
 .inner-text {
  text-align: center;
 }

 .pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1rem;
}

.pagination button {
  margin: 0 0.5rem;
  cursor: pointer;
}

.pagination span {
  margin: 0 0.5rem;
  font-weight: bold;
}
</style>