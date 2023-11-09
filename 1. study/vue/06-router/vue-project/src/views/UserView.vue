<!-- 컴포넌트는 맞지만 router view에 직접적으로 연결될 컴포넌트여서 이름은 UserView로 했고, views 라는 폴더에 위치 시킴 -->


<template>
  <div>
    <h1>UserView</h1>
    <!-- 라우트 객체는 전역으로 제공을 하는 것이라서 $가 붙어있는 속성 값 -->
    <!-- 결과는 동일해도 아래 방식을 권장 -->
    <h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
    <h2>{{ userId }}번 유저의 페이지입니다.</h2>
    <button @click="goHome">홈으로!!</button>
    <button @click="goAnotherUser">100번 유저 페이지로!</button>
  </div>
</template>

<script setup>
  // JS에서는 $라는 속성 x(emit 참조)
  // 그래서 JS에서는 import 필요
  // 여기서 'vue-router'를 사용가능한 이유는 우리의 프로젝트에 이미 'vue-router'가 들어가 있기 때문.
  import {ref} from 'vue'
  import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const userId = ref(route.params.id) // 여기에 있는 route와 위의 $route랑 동일한 것임.

  // 프로그래밍 방식 네비게이션
  
  const router = useRouter()

  const goHome = function(){
    // router.push({ name : 'home' })
    router.replace({ name : 'home' })
  }

  // In-component Guard
  // 1. onBeforeRouteLeave
  onBeforeRouteLeave((to, from)=>{
    const answer =  window.confirm('정말 떠나실 건가요?') //confirm은 리턴값을 가지고 있다.(확인 or 취소에 대한.)
    if (answer === false) {
      return false
    }
  })
  // 2. onBeforeRouteUpdate(url 변경은 없고 variable만 변화가 있는 경우)
  const goAnotherUser = function(){
    router.push({name:'user', params:{id:100} })
  }

  // 못 따라가는 데이터를 처리
  // 왜 못 따라감? 반응형 변수를 직접 수정해주지 않아서.
  // 반응형 변수를 따라가서 변경해주자!
  onBeforeRouteUpdate((to, from)=>{
    userId.value = to.params.id
  })


</script>

<style lang="scss" scoped>

</style>