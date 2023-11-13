<template>
  <div>
    <form @submit.prevent="createTodo()">
      <input type="text"
      v-model="todoText"
      >
      <input type="submit">
    </form>

    <!-- <form @submit.prevent="createTodo2(todoText2)">
      <input type="text"
      v-model="todoText2"
      >
      <input type="submit">
    </form>

    <form @submit.prevent="createTodo3(todoText3)" ref="formElem">
      <input type="text"
      v-model="todoText3"
      >
      <input type="submit">
    </form> -->
  </div>
</template>

<script setup>

import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue'

const todoText = ref('')
const todoText2 = ref('')
const todoText3 = ref('')
const store = useCounterStore()

// 방법 1
const createTodo = function(){
  store.addTodo(todoText.value)
  todoText.value = ''
}

// 방법 2 (방법 2의 방식으로는 초기화가 되지 않는 이유??)
// Vue가 반응성(reactivity) 및 변수 할당을 처리하는 방식 때문
// 함수 내에서만 todoText2의 값을 비우고 원래의 참조에 영향을 미치지 않습니다.

// 이를 해결하기 위해 .value를 달면 또 다른 문제점이 발생함.
// "todoText2"가 문자열(string)인데 이에 대해 "value" 속성을 설정하려고 하기 때문에 오류가 발생

const createTodo2 = function(todoText2){
  store.addTodo(todoText2)
  todoText2 = ''
}


// "방법 1"의 경우 todoText.value = ''는 반응성 있는 ref를 직접 수정하여 값을 지우므로 해당 값에 연결된 템플릿에서 업데이트됩니다.

// "방법 2"의 경우 todoText2 = ''는 로컬 함수 매개변수 todoText2를 재할당하며 함수 외부의 원래 참조에 영향을 미치지 않습니다. 함수 외부의 원래 todoText2를 지우려면 value 속성을 사용해야 합니다. 이렇게 하면 원래 todoText2를 함수 외부에서 올바르게 지울 수 있으며, 이는 "방법 1"과 유사한 반응성을 갖게 됩니다.

// 방법 3

// const formElem = ref(null)

// const createTodo3 = function (todoText3) {
//   store.addTodo(todoText3)
//   formElem.value.reset()
// }

</script>

<style scoped>

</style>