<template>
  <div>
    <div>
      <p>{{ pk }}번 문제</p>
      <h2>정답 확인</h2>
    </div>
    <div>
      <p>{{ isCorrect ? '정답' : '오답' }}</p>
      <p>나의 제출 답안 : {{ userAnswer }}</p>
      <p>정답 : {{ answer }}</p>
    </div>
  </div>
</template>

<script setup>
  import {computed} from 'vue'
  import {useRoute} from 'vue-router'
  const route = useRoute()
  // const pk = route.params.pk
  // const answer = route.params.answer
  const { pk, answer } = route.params
  const { userAnswer } = route.query
  const isCorrect = computed(()=>{
    return userAnswer === answer
  })
</script>

<style scoped>

</style>