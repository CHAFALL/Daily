<template>
  <div>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script setup>
import CommentListItem from '@/components/community/CommentListItem.vue'
import axios from 'axios'
import {ref, onMounted, watch } from 'vue'
import { useCounterStore } from '@/stores/counter';
const comments = ref([])
const store = useCounterStore()

const props = defineProps({
  review: Object,
})


// DRF에 comment 조회하기
// 해당 코드에서 onMounted을 안 쓴 이유:
// 너무 초기에 받아오려다 보니 어쩌다 한 번씩 받아지더라....


// 추가로 고쳐야 할 점... 댓글 추가 할 시 바로 업데이트 안됨..

watch(() => props.review, (newReview, oldReview) => {
  if (newReview && newReview.id && newReview !== oldReview) {
    axios({
      method: 'get',
      url: `${store.API_URL}/community/reviews/${newReview.id}/comments/`,
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

<style lang="scss" scoped>
</style>