<template>
  <div class="article-detail">
    <h1 class="navbar">Article Detail</h1>
    <div v-if="article" class="article-content">
      <div class="title">
        <h1 class="article-title">{{ article.title }}</h1>
        <div class="btn-group" v-if="isCreater">
          <div>
            <button @click="articleDelete" class="btn delete">삭제</button>
            <button @click="router.push({name: 'update', params:{id: route.params.id}})" class="btn update">수정</button>
          </div>
        </div>
      </div>

      
      <div class="like-count">
        <span class="article-info" style="font-size: 20px; cursor: pointer;" @click="router.push({name: 'profile', params: { username: article.user.username }})"><strong>{{ article.user.username }}</strong></span>
        <span @click="like" class="btn like">{{ isLiked ? '❤️' : '🤍' }}</span> 
      </div>
      <div class="title">
        <p class="article-info" style="color: #a7a7a7;">{{ formatDate(article.created_at) }}</p>
        <div class="count">
          {{ likeCount }}
        </div>
      </div>
      <p class="article-content">{{ article.content }}</p>
      <br>
      <ArticleDetailComment :id="article.id"/>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import { useRouter } from 'vue-router'
import ArticleDetailComment from '@/components/Article/ArticleDetailComment.vue'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const article = ref(null)
const isCreater = ref(false)
const likeCount = ref(null)
const isLiked = ref(false)

// 게시글 호출하는 함수
onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/community/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      article.value = res.data
      for (const user of res.data.like_users) {
        if (userStore.user === user.username) {
          isLiked.value = true
        }
      }
      if (article.value.user.username === userStore.user) {
        isCreater.value = true
      }
      likeCount.value = article.value.like_users.length
    })
    .catch(err => console.log(err))
})

// 게시글 삭제 함수
const articleDelete = function () {
  const answer = window.confirm('게시글을 삭제하시겠습니까?')
  if (answer) {
    axios({
      method: 'delete',
      url: `${userStore.API_URL}/api/v1/community/${route.params.id}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        router.push({name: 'articles'})
      })
  }
}

// 좋아요
const like = function() {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/api/v1/community/${route.params.id}/like/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      if (res.data.isLiked) {
        likeCount.value++
        isLiked.value = res.data.isLiked
      } else {
        likeCount.value--
        isLiked.value = res.data.isLiked
      }
    })
    .catch(err => console.log(err))
}

const formatDate = (timestamp) => {
  const date = new Date(timestamp);
  return date.toLocaleString();
}

</script>

<style scoped>
.like-count {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.article-detail {
  max-width: 800px;
  margin: 0 auto;
  padding: 30px;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-family: 'Noto Sans KR', sans-serif;
  color: #333;
}

.article-detail h2 {
  margin-bottom: 20px;
  text-align: center;
  color: #444;
}

.article-content {
  padding: 20px;
  background-color: #fff;
  border-radius: 3%;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}



.btn {
  margin-left: 10px;
  /* padding: 28px 20px; */
  border: none;
  border-radius: 20%;
  cursor: pointer;
}

.btn-like {
  background-color: #ffffff;
  outline: none;

}

.btn.delete {
  text-align: center;
  background-color: #c7c7c7;
  transition: background-color .3s;
  color: black;
  font-weight: bold;
  height: 40px;
  width: auto;  
}

.btn.delete:hover {
  background-color: #a7a7a7;

}

.btn.update {
  background-color: #c7c7c7;
  transition: background-color .3s;
  color: black;
  font-weight: bold;
  height: 40px;
  width: auto;
}

.btn.update:hover {
  background-color: #a7a7a7;
}

.article-title {
  font-size: 30px;
  margin-bottom: 10px;
  color: #444;
}

.article-info {
  margin-top: 15px;
  font-size: 16px;
  margin-bottom: 5px;
}

.article-content {
  margin-top: 20px;
  font-size: 18px;
  line-height: 1.5;
  color: #666;
}

.btn-group {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.title {
  display: flex;
  justify-content: space-between;
}

.count {
  margin-right: 7px; 
  font-size: 15px;
  color: #a9a9a9;
}
</style>