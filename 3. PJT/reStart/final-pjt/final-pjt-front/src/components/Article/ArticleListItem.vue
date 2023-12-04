<template>
  <div
    class="article-card"
    @click="router.push({name: 'article', params:{id: article.id}})"
  >
    <div class="article-row">
      <p class="article-info">{{ article.id }}</p>
      <h3 class="article-title">{{ article.title }}</h3>
      <p class="article-info">{{ article.user.username }}</p>
      <p class="article-info">{{ formatDate(article.created_at) }}</p>
      <p class="article-info">{{ article.like_users.length }}</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
const router = useRouter()

const props = defineProps({
  article: Object,
  index: Number,
})

const userStore = useUserStore()
const user = userStore.user

const formatDate = (timestamp) => {
  const date = new Date(timestamp);
  return date.toLocaleString();
}
</script>

<style scoped>
.article-card {
  font-family: 'Noto Sans KR', sans-serif;
  cursor: pointer;
  padding: 10px 20px;
  border-bottom: 1px solid #eee;
  transition: all .3s ease-in-out;
}

.article-card:hover {
  background-color: #f8f9fa;
}

.article-row {
  display: flex;
  justify-content: space-between;
}

.article-title {
  font-size: 16px;
  margin-bottom: 5px;
  color: #6c757d;
}

.article-info, .article-title {
  font-size: 14px;
  margin-bottom: 3px;
  color: #6c757d;
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif;
}


.article-info:nth-child(1), .article-title:nth-child(1) { 
  flex: 0 0 10%;  /* 글 번호 */
}
.article-info:nth-child(2), .article-title:nth-child(2) { 
  flex: 0 0 50%;  /* 제목 */
}
.article-info:nth-child(3), .article-title:nth-child(3) { 
  flex: 0 0 20%;  /* 작성자 */
}
.article-info:nth-child(4), .article-title:nth-child(4) { 
  flex: 0 0 10%;  /* 작성일 */
}
.article-info:nth-child(5), .article-title:nth-child(5) { 
  flex: 0 0 10%;  /* 좋아요 */
}
</style>

