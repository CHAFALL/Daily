<template>
  <div class="recomment-margin">
    <!-- <h4>대댓글</h4> -->
    <div v-if="recomments && recomments.length > 0" >
      <h5>💬 대댓글 {{ recomments.length }}개</h5>
      <hr>
      <div class="scroll-bar">
      <RecommentItem 
        v-for="recomment in recomments"
        :key="recomment.id"
        :recomment="recomment"
        :articleId="props.articleId"
        @delete-event="reload"
      />
      </div>
    </div>
    <form @submit.prevent="createReComment">
      <div class="in-line">
        <textarea name="recomment" id="recomment" placeholder="대댓글을 남겨보세요" cols="30" rows="5" v-model=content></textarea>
        <button type="submit" name="recomment" class="button">작성</button>
      </div>
    </form>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import RecommentItem from '@/components/Article/ArticleDetailCommentRecommentItem.vue'
const userStore = useUserStore()
const props = defineProps({
  commentId: Number,
  articleId: Number,
})
const content = ref(null)
const recomments = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/community/${props.articleId}/comments/${props.commentId}/recomment/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      recomments.value = res.data
    })
    .catch(err => console.log(err))
})

const reload = function () {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/community/${props.articleId}/comments/${props.commentId}/recomment/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      recomments.value = res.data
    })
    .catch(err => console.log(err))
}

const createReComment = function () {
  if (content.value && content.value.trim().length > 0) {
    axios({
      method: 'post',
      url: `${userStore.API_URL}/api/v1/community/${props.articleId}/comments/${props.commentId}/recomment/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      },
      data: {
        content: content.value
      }
    })
      .then(res => {
        recomments.value.push(res.data)
        content.value = ''
      })
      .catch(err => console.log(err))
  } else {
    window.alert('대댓글의 내용이 비어 있습니다.')
  }
}
</script>

<style scoped>
.scroll-bar {
  max-height: 300px;
  overflow-y: scroll;
}
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
  width: 48px;
}

.button:hover {
  background-color: rgb(197, 197, 197);
}

.recomment-margin {
  margin-left: 30px;
}
</style>