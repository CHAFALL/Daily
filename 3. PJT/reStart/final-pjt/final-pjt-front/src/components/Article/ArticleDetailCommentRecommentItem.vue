<template>
  <div>
    <div class="like-position">
      <span style="cursor: pointer; font-size: 15px;" @click="router.push({name: 'profile', params:{username: recomment.user.username}})"><strong>{{ recomment.user.username }}</strong></span> 
      <span @click="like" class="btn-like">{{ isLiked ? '❤️' : '🤍' }}</span> 
    </div>
    <div class="like-count">
      <p style="font-size: 16px;">{{ recomment.content }}</p>
      <p style="margin-right: 9px; font-size: 12px; color: #a9a9a9">{{ likeCount }}</p>
    </div>
    <p style="font-size: 14px; color: grey; margin-top: 0px;">{{ formatDate(recomment.created_at) }}</p>
    
    <!-- 현재 사용자와 댓글 작성자가 같은 경우에만 수정 및 삭제 -->
    <div v-if="recomment.user.username === userStore.user">
      <form v-if="isUpdate" @submit.prevent="updateComment">
        <input type="text" v-model="content">
        <button type="submit" class="delete-btn">UPDATE</button>
      </form>
      <button v-else @click="deleteComment" class="delete-btn">DELETE</button>
      <button @click="isUpdate=!isUpdate" class="delete-btn">{{ isUpdate ? 'CANCEL' : 'UPDATE' }}</button>
    </div>
    <hr>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
const userStore = useUserStore()
const router = useRouter()

const emit = defineEmits(['deleteEvent'])
const props = defineProps({
  recomment: Object,
  articleId: Number,
})
const isUpdate = ref(false)
const content = ref(props.recomment.content)
const isLiked = ref(false)
const likeCount = ref()

watch(() => isUpdate.value, () => {
  content.value = props.recomment.content
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/community/${props.articleId}/comments/${props.recomment.id}/like/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      isLiked.value = res.data.isLiked
      likeCount.value = res.data.likeCount
    })
    .catch(err => console.log(err))
})

const deleteComment = function () {
  const answer = window.confirm('해당 대댓글을 삭제하시겠습니까?')
  if (answer) {
    axios({
      method: 'delete',
      url: `${userStore.API_URL}/api/v1/community/${props.articleId}/comments/${props.recomment.id}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        emit('deleteEvent')
      })
      .catch(err => console.log(err))
  }
}

const updateComment = function () {
  if (content.value && content.value.trim().length > 0) {
    axios({
      method: 'put',
      url: `${userStore.API_URL}/api/v1/community/${props.articleId}/comments/${props.recomment.id}/`,
      data: { content: content.value },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        props.recomment.content = res.data.content
        isUpdate.value = false
      })
      .catch(err => console.log(err))
  } else {
    window.alert('수정하려는 대댓글의 내용이 비어있습니다.')
  }
}

const like = function () {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/api/v1/community/${props.articleId}/comments/${props.recomment.id}/like/`,
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
.btn-like {
  cursor: pointer;
}

hr {
  border-top: .1px solid lightgrey;
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


.like-position {
  display: flex;
  justify-content: space-between;
}

.like-count {
  display: flex;
  justify-content: space-between;
}
</style>
