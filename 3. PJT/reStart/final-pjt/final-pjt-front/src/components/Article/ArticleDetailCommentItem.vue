<template>
  <!-- 대댓글이 아닌 댓글만 출력되게 함 -->
  <div v-if="comment.parent_comment === null">
  <!-- <div> -->
    <div class="like-position">
      <span style="cursor: pointer;" @click="router.push({name: 'profile', params:{username: comment.user.username}})"><strong>{{ comment.user.username }}</strong></span> 
      <span @click="like" class="btn-like">{{ isLiked ? '❤️' : '🤍' }}</span> 
    </div>
    <div class="like-count">
      <p style="font-size: 17px;">{{ comment.content }}</p>
      <p style="margin-right: 8px; font-size: 15px; color: #a9a9a9;">{{ likeCount }}</p>
    </div>
    <p style="font-size: 14px; color: grey; margin-top: 0px;">{{ formatDate(comment.created_at) }}</p>
    <!-- 현재 사용자와 댓글 작성자가 같은 경우에만 삭제 및 수정이 가능하도록 함 -->
    <div v-if="comment.user.username === userStore.user">
      <form v-if="isUpdate" @submit.prevent="updateComment()">
        <input type="text" v-model="content">
        <button type="submit" class="update-btn">UPDATE</button>
      </form>
      <button v-else @click="deleteComment" class="delete-btn">DELETE</button>
      <button @click="isUpdate=!isUpdate" class="update-btn">{{ isUpdate ? 'CANCEL' : 'UPDATE' }}</button>
    </div>
    <!-- 작성자가 아니라면 좋아요 기능이 나타나게 함 -->

    <br>
    <span @click="isRecomment=!isRecomment" style="font-size: 15px; cursor: pointer;"> 더보기...</span>
  <div class="recomment-action" :style="{ maxHeight: isRecomment ? '500px' : '0' }">
    <Recomment v-if="isRecomment" :commentId="comment.id" :articleId="props.id"/>
  </div>
  <hr style="border-top: 0.5px solid lightgrey;">
</div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import Recomment from '@/components/Article/ArticleDetailCommentRecomment.vue'
const userStore = useUserStore()
const router = useRouter()

const props = defineProps({
  comment: Object,
  id: Number,
})
const emit = defineEmits(['deleteEvent'])
const isUpdate = ref(false)
const content = ref(props.comment.content)
const isLiked = ref(false)
const likeCount = ref()
const isRecomment = ref(false)

watch(() => isUpdate.value, () => {
  content.value = props.comment.content
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/community/${props.id}/comments/${props.comment.id}/like/`,
    headers:{
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      isLiked.value = res.data.isLiked
      likeCount.value = res.data.likeCount
    })
    .catch(err => console.log(err))
})

// 댓글 수정 함수
const updateComment = function () {
  if (content.value && content.value.trim().length > 0) {
    axios({
      method: 'put',
      url: `${userStore.API_URL}/api/v1/community/${props.id}/comments/${props.comment.id}/`,
      data: { content: content.value },
      headers:{
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        props.comment.content = res.data.content
        isUpdate.value = false
      })
      .catch(err => console.log(err))
  } else {
    window.alert('수정하려는 댓글의 내용이 비어 있습니다.')
  }
}

// 댓글 삭제 함수
const deleteComment = function () {
  const answer = window.confirm('게시글을 삭제하시겠습니까?')
  if (answer) {
    axios({
      method: 'delete',
      url: `${userStore.API_URL}/api/v1/community/${props.id}/comments/${props.comment.id}/`,
      headers:{
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        emit('deleteEvent')
      })
      .catch(err => console.log(err))
  }
}

// 좋아요
const like = function () {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/api/v1/community/${props.id}/comments/${props.comment.id}/like/`,
    headers:{
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      isLiked.value = res.data.isLiked
      likeCount.value = res.data.likeCount
    })
    .catch(err => console.log(err))
}

// 시간 수정
const formatDate = (timestamp) => {
  const date = new Date(timestamp);
  return date.toLocaleString();
}
</script>

<style scoped>
.like-position {
  display: flex;
  justify-content: space-between;
}
.btn-like {
  cursor: pointer;
}

.delete-btn {
  border: 3px solid lightgrey;
  background-color: white;
  height: 30px;
  font-size: 12px;
  margin-right: 0px;
  border-radius: 10px;
  transition: .4s;
}

.delete-btn:hover {
  background-color: lightgrey;
  transform: scale(1.1);
  color: white;
}

.update-btn {
  border: 3px solid lightgrey;
  background-color: white;
  height: 30px;
  font-size: 12px;
  transition: .3s ease;
  border-radius: 10px;
}

.update-btn:hover{
  background-color: lightgrey;
  transform: scale(1.2);
  color: white;
}

.recomment-action {
  overflow: hidden;
  transition: max-height 0.5s ease;
}

.like-count {
  display: flex;
  justify-content: space-between;
}
</style>