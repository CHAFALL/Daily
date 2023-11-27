<template>
  <div style="margin-top: 20px;">
    <div v-if="averageRank !== null" class="average-rank">
      시청자 평점 : {{ averageRank }}
    </div>
    <div v-else class="no-comments">
      <p>아직 아무도 평가하지 않았습니다.</p>
    </div>

    <MovieReviewListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
  
</template>

<script setup>
import axios from 'axios'
import {ref, onMounted, watch, computed } from 'vue'
import { useCounterStore } from '@/stores/counter';
import MovieReviewListItem from './MovieReviewListItem.vue';
const comments = ref([])
const store = useCounterStore()

const props = defineProps({
  movie: Object,
})


const averageRank = computed(() => {
  if (comments.value.length === 0) {
    return null;
  }
  const sum = comments.value.reduce((total, comment) => total + comment.rank, 0);
  return Math.round((sum / comments.value.length)*10)/10;
});



// DRF에 comment 조회하기
// 해당 코드에서 onMounted을 안 쓴 이유:
// 너무 초기에 받아오려다 보니 어쩌다 한 번씩 받아지더라....
// onBeforeMount가 있다는데???


// 추가로 고쳐야 할 점... 댓글 추가 할 시 바로 업데이트 안됨..

watch(() => props.movie, (newMovie, oldMovie) => {
  if (newMovie && newMovie.id && newMovie !== oldMovie) {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/movies/${newMovie.id}/movie_reviews/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((res) => {
      console.log(res)
      comments.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }
})

</script>

<style scoped>
.average-rank {
  color: #007BFF; /* 원하는 글씨 색상 설정 */
}

.no-comments {
  color: #6C757D; /* 원하는 글씨 색상 설정 */
}
</style>