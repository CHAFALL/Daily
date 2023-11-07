<template>
  <div>
    <!-- JS에서 직접 선택할 수 있게 태그해둔 느낌(ref="input") -->
    <input type="text" ref="ssafy">
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'

// 여기서 활용하는 변수명이 ref='xxx'와 같아야 한다.
// 그리고 여기에 들어가는 ref()는 아무 의미 x
const ssafy = ref()

onMounted(()=>{
  console.log(ssafy.value)
})


</script>

<style scoped>

</style>