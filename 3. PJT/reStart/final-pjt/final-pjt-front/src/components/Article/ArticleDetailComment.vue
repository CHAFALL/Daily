<template>
  <div>
    <!-- 댓글 작성 -->
    <form @submit.prevent="createComment">
        <div class="in-line">
          <textarea id="comment" name="comment" v-model="content" placeholder="댓글을 남겨보세요"></textarea>
          <button type="submit" name="comment" class="button">작성</button>
        </div>
      </form>

    <!-- 댓글 목록 -->
    <template v-if="comments">
      <h3>💬 댓글 {{ commentCount }}개</h3>
      <hr >
      <ArticleDetailCommentItem 
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
        :id="props.id"
        @delete-event="reload"
      />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import ArticleDetailCommentItem from './ArticleDetailCommentItem.vue';
const userStore = useUserStore()
const comments = ref(null)
const content = ref(null)
const commentCount = ref(null)

const props = defineProps({
  id: Number,
})

// 페이지가 마운트 되면 댓글 목록 가지고 오기
onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/community/${props.id}/comments/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      commentCount.value = res.data.filter((comment) => {
        if (comment.parent_comment === null) {
          return comment
        }
      }).length
      comments.value = res.data
    })
    .catch(err => console.log(err))
})

const reload = function () {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/community/${props.id}/comments/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      comments.value = res.data
      commentCount.value -= 1
    })
    .catch(err => console.log(err))
}

// 댓글 작성 함수
const createComment = function () {
  if (content.value && content.value.trim().length > 0) {
    axios({
      method: 'post',
      url: `${userStore.API_URL}/api/v1/community/${props.id}/comments/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      },
      data: {
        content: content.value
      }
    })
      .then(res => {
        comments.value.push(res.data)
        commentCount.value += 1
        content.value = ''
      })
      .catch(err => console.log(err))
  } else {
    window.alert('댓글의 내용이 비어 있습니다.')
  }
}
</script>

<style scoped>
  .in-line {
    display: flex;
    align-items: center;
  }

  textarea{
    width: 690px;
    height: 70px;
    font-size: 15px;
    border: 0;
    border-radius: 15px;
    outline: none;
    padding-left: 10px;
    background-color: rgb(240, 240, 240);
  }

  .button {
  background-color: rgb(122, 122, 122);
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 8px 10px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-left: 8px;
}

.button:hover {
  background-color: rgb(197, 197, 197);
}

</style>