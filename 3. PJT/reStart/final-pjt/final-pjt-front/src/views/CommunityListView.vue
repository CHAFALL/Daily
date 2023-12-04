<template>
  <div class="community-container">
  <h1 class="navbar">Community</h1>
    <div class="wrapper">
      <hr>
      <div class="text-wrapper">
        <p>글 번호</p> <!-- 추가 -->
        <p>제목</p>
        <p>작성자</p>
        <p>작성일</p>
        <p>좋아요</p>
      </div>
      <hr>
      <ArticleList class="article-box"/>
      <div class="buttons">
        <button class="btn-hover" @click="router.push({name: 'create'})">Create</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import ArticleList from '@/components/Article/ArticleList.vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
import { useUserStore } from '@/stores/user'
import { onMounted } from 'vue'

const router = useRouter()
const articleStore = useArticleStore()
const userStore = useUserStore()

onMounted(() => {
  articleStore.getArticles(userStore.token)
})


</script>

<style scoped>

.community-container {
  max-width: 1300px;
  margin: 0 auto;
  background-color: #f5f5f5;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-family: 'Noto Sans KR', sans-serif;
  color: #333;
  padding: 30px;
}

.wrapper {
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.text-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 10px 20px;
  background-color: #f8f9fa;
  font-weight: 60px;
}

.text-wrapper p {
  flex: 1;
  text-align: center;
}

.text-wrapper p:nth-child(1) { flex: 0 0 10%; } /* 글 번호 */
.text-wrapper p:nth-child(2) { flex: 0 0 50%; } /* 제목 */
.text-wrapper p:nth-child(3) { flex: 0 0 20%; } /* 작성자 */
.text-wrapper p:nth-child(4) { flex: 0 0 10%; } /* 작성일 */
.text-wrapper p:nth-child(5) { flex: 0 0 10%; } /* 좋아요 */

.buttons {
  text-align: center;
  padding: 20px;
}

.btn-hover {
  width: 100px;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  cursor: pointer;
  margin: 20px;
  height: 40px;
  text-align: center;
  border: none;
  background-size: 300% 100%;
  border-radius: 50px;
  transition: all .4s ease-in-out;
  background-color: #6c757d;
}

</style>