<template>
  <div class="container">
    <div class="create-form">
      <h1>Create</h1>
      <form @submit.prevent="createArticle" class="form">
        <div class="align">
          <label for="title" class="form-label">제목</label>
          <input type="text" id="title" v-model="title" placeholder="제목을 입력하세요" class="form-input">
        </div>
        <div class="align">
          <label for="content" class="form-label">내용  </label>
          <textarea id="content" v-model="content" placeholder="내용을 입력하세요" class="form-textarea"></textarea>
        </div>
        <div class="form-btn">
          <button @click="router.push({name: 'articles'})" class="submit-btn">뒤로가기</button>
          <button class="submit-btn">작성하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/articles';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';
import axios from 'axios';

const articleStore = useArticleStore();
const userStore = useUserStore();
const router = useRouter();
const title = ref('');
const content = ref('');

const createArticle = function () {
  if (title.value.trim() && content.value.trim()) {
    axios({
      method: 'post',
      url: `${articleStore.API_URL}/api/v1/community/`,
      data: {
        title: title.value,
        content: content.value,
      },
      headers: { Authorization: `Token ${userStore.token}` },
    })
      .then((res) => {
        router.push({ name: 'article', params: { id: res.data.id } })
      })
      .catch((err) => console.error(err))
  } else {
    window.alert('Please fill in both the title and content.')
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

.align{
  display: flex;
  justify-content: space-between;
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

.form-textarea{
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