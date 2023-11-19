<template>
  <div>
    <h2>퀴즈 생성</h2>
    <form @submit.prevent="createQuiz">
      <label for="question">문제</label><br>
      <textarea
      id="question" 
      cols="50" 
      rows="5" 
      v-model="newQuiz.question"
      @input="onChange"
      ></textarea>

      <label for="answer">답안</label><br>
      <input 
      type="text" 
      id="answer" 
      v-model="newQuiz.answer"
      @input="onChange"
      >
      
      <button>퀴즈 생성</button>
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
const newQuiz = ref({
  question: '',
  answer:'',
})

const emit =defineEmits(['createQuiz', 'onChange'])
const createQuiz= function() {
  if(newQuiz.value.question && newQuiz.value.answer){
    emit('createQuiz', newQuiz.value)
    newQuiz.value.question = ''
    newQuiz.value.answer = ''
  }
}
const onChange = function () {
  emit('onChange',newQuiz.value)
}

</script>

<style scoped>

</style>