<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
    <h2>{{ userId }}번 유저의 페이지입니다.</h2>
    <button @click="goHome">홈으로!!</button>
    <button @click="routeUpdate">100번째 페이지</button>
  </div>
</template>

<script setup>
  import {ref} from 'vue'
  import { onBeforeRouteLeave, onBeforeRouteUpdate, useRoute, useRouter } from 'vue-router'

  const route = useRoute()
  const router = useRouter()
  
  
  const userId = ref(route.params.id)

  const goHome = function () {
    // router.push({ name:'home' })
    router.push({ name:'user', params: {id:'alice'} })
    // router.replace({ name:'home' })
  }

  onBeforeRouteLeave((to, from)=>{
    const ans = window.confirm('정말 떠나실 건가요?')
    if (ans === false){
      return false
    }
  })

  const routeUpdate = function () {
    router.push({name:'user', params: {id:100} })
  }
  
  onBeforeRouteUpdate((to, from)=>{
    userId.value = to.params.id
  })
</script>

<style scoped>

</style>