<template>
  <div class="container">
    <div class="create-form">
    <h1>Update</h1>
    <div v-if="article">
      <form @submit.prevent="articleUpdate">
        <div class="align">
          <label for="title" class="form-label">제목</label>
          <input type="text" id="title" v-model="article.title" placeholder="제목을 입력하세요" class="form-input">
        </div>
        <div class="align">
          <label for="content" class="form-label">내용</label>
          <textarea id="content" cols="30" rows="10" v-model="article.content" placeholder="내용을 입력하세요" class="form-textarea"></textarea>
        </div>
        <div class="form-btn">
          <button @click="router.push({name: 'articles'})" class="submit-btn">뒤로가기</button>
          <button class="submit-btn">작성하기</button>
        </div>
      </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
const articleStore = useArticleStore()
const userStore = useUserStore()

const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${articleStore.API_URL}/api/v1/community/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      if (res.data.user.username === userStore.user) {
        article.value = res.data
      } else {
        window.alert('해당 글의 작성자가 아닙니다.')
        router.push({name: 'articles'})
      }
    })
    .catch(err => console.log(err))
})

const articleUpdate = function () {
  if ((article.value.title && article.value.title.trim().length > 0) && (article.value.content && article.value.content.trim().length > 0)) {
    axios({
      method: 'put',
      url: `${articleStore.API_URL}/api/v1/community/${route.params.id}/`,
      data: {
        title: article.value.title,
        content: article.value.content
      },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        router.push({name: 'article', params:{id: res.data.id}})
      })
      .catch(err => console.log(err))
  } else {
    window.alert('제목과 내용을 채워주세요.')
  }
}
</script>

<style scoped>
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin-top: -100px;
  }

  .create-form {
    max-width: 600px;
    width: 600px;
    padding: 20px;
    border: 1px solid lightgrey;
    border-radius: 15px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    background-color: #fff;
  }

  .align {
    display: flex;
    justify-content: space-between;
  }

  .form {
    display: flex;
    flex-direction: column;
  }

  .form-label {
    margin-top: 10px;
    font-weight: bold;
    color: #555;
  }

  .form-input,
  .form-textarea {
    width: 550px;
    padding: 8px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 1px solid lightgrey;
    border-radius: 10px;
  }

  .form-textarea {
    height: 300px;
  }

  .submit-btn {
    border: 1px solid lightgrey;
    color: black;
    width: 120px;
    height: 40px;
    background-color: white;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
  }

  .submit-btn:hover {
    border: 2px solid lightgrey;
    background-color: rgb(238, 238, 238);
  }

  .form-btn {
    margin-top: 15px;
    display: flex;
    justify-content: space-between;
  }
  
</style>