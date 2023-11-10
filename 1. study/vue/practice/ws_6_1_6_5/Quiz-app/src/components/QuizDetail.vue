<template>
  <div>
    <h3>{{ quiz.pk }}번 문제. {{ quiz.question }}</h3>
    <label :for="'answer'+quiz.pk">정답 입력</label>
    <input 
    type="text" 
    :id="'answer'+quiz.pk"
    v-model="userAnswer"
    @keyup.enter="submitAnswer(quiz)"
    >
  </div>
</template>

<script setup>

  import {ref} from 'vue'
  import { useRouter } from 'vue-router';

  defineProps({
    quiz: Object,
  })

  const userAnswer=ref('')

  const router = useRouter()
  const submitAnswer = function(quiz){
    const ans = window.confirm(`${userAnswer.value}를 답안으로 제출하시겠습니까?`)
    if (ans){
      router.push({
        name:'answer',
        params: {
          pk : quiz.pk,
          answer : quiz.answer,
        },
        query: {
          userAnswer: userAnswer.value
        }
      })
    } else {
      userAnswer.value=''
    }
  }
</script>

<style scoped>

</style>