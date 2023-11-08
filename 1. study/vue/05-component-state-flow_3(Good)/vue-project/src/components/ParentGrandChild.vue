<template>
  <div>
    <p>{{ myMsg }}</p>
    <button @click="ssafy">이름 변경!</button>
  </div>
</template>

<script setup>
// 이렇게 Props를 선언해줘야 템플릿에서 사용 가능!!
defineProps ({
  myMsg : String,
})

// emit 이벤트 이름을 이렇게 정의를 해줬기 때문에 사용가능
const emit = defineEmits(['updateName'])

const ssafy = function () {
  emit('updateName')
}

</script>

<style scoped>

</style>