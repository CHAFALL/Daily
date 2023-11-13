<template>
  <div>
    <form @submit.prevent="createTodo()">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import {ref} from 'vue'

const store = useCounterStore()
const todoText = ref('')

const createTodo = function () {
  store.addTodo(todoText.value)
  todoText.value = ''
  // 교재에 다른 방식도 있음을 알 수 있다(초기화 방법)
}

// 아래와 같이도 가능. 단 template 부분에서도 인자로 todoText 넣어주기
// 이렇게 하면 .value 안 넣어줘도 됨 (왜냐하면 함수의 인자 우선순위가 더 높아서 (함수의 인자 - 객체가 아니라 문자열로 들어감))

// const createTodo = function (todoText) {
//   store.addTodo(todoText)
// }

</script>

<style scoped>

</style>