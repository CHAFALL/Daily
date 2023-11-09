<template>
  <div class='border'>
    <h3>자식 페이지 입니다.</h3>
    <p>이름: {{ child.name }}</p>
    <p>나이: {{ child.age }}</p>
    <p>용돈: {{ child.balance }}</p>
    <button @click="updateBalance">용돈주세요.</button>
  </div>
</template>

<script setup>
  defineProps({
    child : Object,
  })

  const emit = defineEmits(['giveMeAllowance'])
  const updateBalance = function () {
    emit('giveMeAllowance')
  }

// const props = defineProps({
//     child : Object,
//   })

// console.log(props.child)

</script>

<style scoped>

</style>