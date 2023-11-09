<template>
  <div>
    <h1>UserView</h1>
    <!-- 라우트의 매개변수는 컴포넌트에서 $route.params로 참조 가능 -->
    <h2>{{ $route.params.id }} 번 유저의 페이지 입니다.</h2>
    <h2>{{ userId }} 번 유저의 페이지 입니다.</h2>
    <button @click="goHome">홈으로!!</button>
    <button @click="goAnoterUser">100번 유저 페이지로!</button>
  </div>
</template>

<script setup>

import { ref } from 'vue'
// JS에서는 $...가 없다
// 아래처럼 import를 해야 사용 가능!
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';


// 2. 프로그래밍 방식 네비게이션
const router = useRouter()
const goHome = function () {
  router.push({ name : 'home' , params: {username: 'alice'}})
  // router.replace({ name : 'home' })
}

// 1.2 선언적 방식(매개변수 받아오는 part, 2번 방식도 이 방식과 똑같이 받아주면 됨)
const route = useRoute()
const userId = ref(route.params.id)

// route는 객체고 router는 전달하는 네비게이션 느낌.


// In-component Guard
// 1. onBeforeRouteLeave
onBeforeRouteLeave ((to, from)=>{
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false){
    return false
  }
})

// 2. onBeforeRouteUpdate
const goAnoterUser = function () {
  router.push({name : 'user', params: {id : 100}})
  // JS쪽은 렌더링 따라가지 못함(왜냐하면 반응형 변수를 직접 변경해 주지 않아서)
}

// 해결법
onBeforeRouteUpdate ((to, from)=>{
  userId.value = to.params.id
})


</script>

<style scoped>

</style>