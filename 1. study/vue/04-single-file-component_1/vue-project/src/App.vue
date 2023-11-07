<template>
 <h1>App.vue</h1>
 <MyComponent /> 
</template>

<script setup>
// 바로 아래는 상대경로로 한 것.
// import MyComponent from './components/Mycomponent.vue'
import MyComponent from '@/components/Mycomponent.vue'
// 이 @가 어떤 의미를 하냐면, 절대경로 /src를 의미.(이걸 추천. 상대경로는 나중에 힘들어짐.)
</script>

<style scoped>

</style>