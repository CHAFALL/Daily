<template>
  <div class="comment-wrapper">
    <div class="left-content">
      <span style="cursor: pointer;" @click="router.push({name: 'profile', params:{username: comment.user.username}})"><strong>{{ comment.user.username }}</strong></span>
    </div>
    <div class="right-content">
      <div v-if="comment.user.username === userStore.user" class="dropdown-wrapper">
        <div class="dropdown">
          <button class="dropdown-toggle" type="button" @click="toggleDropdown">
            <img src="@/assets/점점점.png" alt="" style="width: 20px; height: auto;">
          </button>
          <div class="dropdown-menu" :class="{ 'show': isDropdownOpen }">
            <form v-if="isUpdate" @submit.prevent="updateComment()">
              <input type="number" min="0" max="5" step="0.5" v-model="score" class="yongsu">
              <input type="text" v-model="updatedContent">
              <!-- <textarea v-model="updatedContent" class="update-textarea"></textarea> -->
              <button type="submit" class="update-button">UPDATE</button>
            </form>
            <p v-else @click="deleteComment" style="cursor: pointer;">DELETE</p>
            <p @click="toggleUpdateMode" style="cursor: pointer;">{{ isUpdate ? 'CANCEL' : 'UPDATE' }}</p>
          </div>
        </div>
      </div>
      <div v-else>
        <button class="dropdown-toggle" type="button" @click="toggleDropdown">
            <img src="@/assets/점점점.png" alt="" style="width: 20px; height: auto;">
        </button>
      </div>
    </div>
  </div>
  <div class="star-rating">
  <div v-for="n in Math.floor(comment.score)">
    <span class="star">★</span>
  </div>
  <div v-if="comment.score - Math.floor(comment.score) > 0">
    <span class="star">☆</span>
  </div>
  <div v-for="n in 5 - Math.ceil(comment.score)">
    <span class="star1"></span>
  </div>
</div>
  <p class="f-f">{{ comment.content }}</p>
  <p style="font-size: 14px; color: grey;">{{ formatDate(comment.created_at) }}</p>
  <hr>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
const userStore = useUserStore()
const router = useRouter()

const props = defineProps({
  comment: Object,
  id: String,
  voteCount: Number,
  voteAvg: Number,
})
const emit = defineEmits(['deleteReview', 'scoreUpdate'])
const isUpdate = ref(false)
const updatedContent = ref(props.comment.content)
const score = ref(props.comment.score)
const content = ref(props.comment.content)

watch(() => isUpdate.value, () => {
  updatedContent.value = props.comment.content
})

const updateComment = function () {
  if (score.value !== null && updatedContent.value && updatedContent.value.trim().length > 0) {
    axios({
      method: 'put',
      url: `${userStore.API_URL}/api/v1/movies/${props.id}/comments/${props.comment.id}/`,
      data: {
        content: updatedContent.value,
        score: score.value
      },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        const updatedVoteTotal = props.voteCount * props.voteAvg - (props.comment.score * 2) + (score.value * 2)
        const updatedVoteAverage = updatedVoteTotal / props.voteCount
        axios({
          method: 'put',
          url:  `${userStore.API_URL}/api/v1/movies/${props.id}/scores/`,
          data: {
            vote_average: updatedVoteAverage
          },
          headers: {
            Authorization: `Token ${userStore.token}`
          }
        })
          .then(res => {
            emit('scoreUpdate')
          })
        props.comment.content = res.data.content
        props.comment.score = res.data.score
        isUpdate.value = false
      })
      .catch(err => console.log(err))
  } else {
    window.alert('수정할 리뷰의 점수와 내용을 모두 적어주세요.')
  }
}

// 리뷰 삭제
const deleteComment = function () {
  const answer = window.confirm('리뷰를 삭제하시겠습니까?')
  if (answer) {
    axios({
      method: 'delete',
      url: `${userStore.API_URL}/api/v1/movies/${props.id}/comments/${props.comment.id}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {     
        const updatedVoteCount = props.voteCount - 1
        const updatedVoteTotal = props.voteCount * props.voteAvg - (props.comment.score * 2)
        const updatedVoteAverage = updatedVoteTotal / updatedVoteCount
        axios({
          method: 'put',
          url:  `${userStore.API_URL}/api/v1/movies/${props.id}/scores/`,
          data: {
            vote_count: updatedVoteCount,
            vote_average: updatedVoteAverage
          },
          headers: {
            Authorization: `Token ${userStore.token}`
          }
        })
          .then(res => {
            emit('deleteReview')
          })
      })
      .catch(err => console.log(err))
  }
}

// 시간 수정
const formatDate = (timestamp) => {
  const date = new Date(timestamp);
  return date.toLocaleString();
}

// 드롭다운
const isDropdownOpen = ref(false)

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const toggleUpdateMode = () => {
  isUpdate.value = !isUpdate.value
  if (isUpdate.value) {
    updatedContent.value = comment.content
  } else {
    updatedContent.value = ''
  }
}
</script>

<style scoped>
.star-rating {
  display: flex;
}

.star {
  color: rgb(247, 210, 2);
}

.star.empty {
  color: lightgray;
}
.comment-wrapper {
  width: 700px;
  display: flex;
  justify-content: space-between;
}

.left-content {
  display: flex;
  align-items: center;
}

.right-content {
  display: flex;
  align-items: center;
  margin-right: -180px;
}

.dropdown-wrapper {
  position: relative;
}

.dropdown-toggle {
  background-color: transparent;
  border: none;
  outline: none;
  cursor: pointer;
}

.dropdown-menu {
  display: none;
  position: absolute;
  width: 50px;
  z-index: 100;
  border: 1px solid lightgrey;
  border-radius: 4px;
  font-size: 12px;
  padding-left: 8px;
}

.dropdown-menu.show {
  display: block;
}

.update-textarea {
  width: 100%;
  height: 70px;
  font-size: 15px;
  border: 0;
  border-radius: 15px;
  outline: none;
  padding-left: 10px;
  background-color: rgb(240, 240, 240);
  margin-bottom: 5px;
}

.update-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  outline: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.update-button:hover {
  background-color: #0056b3;
}

.box {
  background-color: lightgrey;
}

hr {
  background: lightgrey;
  height: 1px;
  border: 0;
  margin-bottom: 10px;
}

.f-f{
  font-family: 'Noto Sans KR', sans-serif;
}


</style>

<style type="text/css">
  input[type="number"]{
    width: 3em;
  }

  input[type="number"] {
      width: 3em;
      height: 10px;
      border: 1px solid #bbbbbb;
      border-radius: 5px;
      padding: 5px;
      font-size: 16px;
      background-color: #ffffff;
      box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
      color: #5e5e5e;
  }

  input[type="number"]:focus {
      outline: none;
      border-color: #969696;
      box-shadow: 0px 0px 5px rgba(136, 136, 136, 0.7);
  }

  input[type="number"]::-webkit-inner-spin-button,
  input[type="number"]::-webkit-outer-spin-button {
      margin: 0;
  }
</style>