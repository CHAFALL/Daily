<template>
  <div>
    <div v-if="userStore.isLogin && comments" class="comment-section">
      <br><h3>💬 리뷰 {{ comments.length }}개</h3>
      <hr class="left-aligned-hr">
      <!-- <h3>리뷰</h3> -->
      
      <MovieDetailCommentItem 
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
        :id="route.params.id"
        :voteCount="props.voteCount"
        :voteAvg="props.voteAvg"
        @score-update="emit('scoreUpdate')"
        @delete-review="reload"
      />
      <form v-if="!havewritten" @submit.prevent="createComment">
        <div class="in-line">
          <input type="number" class="score-selector" min="0" max="5" step="0.5" v-model="score">
          <div class="input-text">
            <textarea id="comment" name="comment" v-model="content" placeholder="리뷰를 남겨보세용~!"></textarea>
            <button type="submit" name="comment" class="button">작성</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import MovieDetailCommentItem from '@/components/Movie/MovieDetailCommentItem.vue'
const userStore = useUserStore()
const route = useRoute()
const comments = ref(null)
const score = ref(null)
const props = defineProps({
  movieId: Number,
  voteCount: Number,
  voteAvg: Number,
})
const emit = defineEmits(['scoreUpdate'])

const content = ref(null)
const havewritten = ref(false)

onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/movies/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      comments.value = res.data
      for (const comment of res.data) {
        if (comment.user.username === userStore.user) {
          havewritten.value = true
        }
      }
    })
    .catch(err => console.log(err))
})

const reload = function () {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/movies/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      comments.value = res.data
      havewritten.value = false
      emit('scoreUpdate')
    })
    .catch(err => console.log(err))
}

const createComment = function () {
  if (score.value !== null && content.value && content.value.trim().length > 0) {
    axios({
      method: 'post',
      url: `${userStore.API_URL}/api/v1/movies/${route.params.id}/comments/`,
      data: {
        content: content.value,
        score: score.value
      },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(res => {
        comments.value.push(res.data)
        havewritten.value = true
        const updatedVoteCount = props.voteCount + 1
        const updateVoteTotal = props.voteCount * props.voteAvg + (score.value * 2)
        const updatedVoteAverage = updateVoteTotal / updatedVoteCount
        axios({
          method: 'put',
          url:  `${userStore.API_URL}/api/v1/movies/${props.movieId}/scores/`,
          data: {
            vote_count: updatedVoteCount,
            vote_average: updatedVoteAverage
          },
          headers: {
            Authorization: `Token ${userStore.token}`
          }
        })
          .then(res => {
            emit('scoreUpdate')
          })
        content.value = null
        score.value = null
      })
      .catch(err => console.log(err))
  } else {
    window.alert('점수와 내용을 모두 적어주세요.')
  }
}
</script>

<style scoped>
  .in-line {
    display: flex;
    flex-direction: column;
  }
  .input-text {
    display: flex;
    align-items: center;
    margin-top: 10px;
  }
  .comment-section {
    width: 900px;
  }

  hr {
    border-top: 1.5px solid lightgrey;
  }

  textarea{
    width: 800px;
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
  outline: none;
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