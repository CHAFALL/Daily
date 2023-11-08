<template>
  <div>
    <h3>자식 페이지 입니다.</h3>
    <p>이름: {{ childName }}</p>
    <p>나이: {{ childAge }}</p>
    <p>용돈: {{ childBalance }}</p>
    <button @click="giveMeAllowance">용돈주세요.</button>

  </div>
</template>

<script setup>
  const props = defineProps({
    childName : String,
    childAge : Number,
    childBalance : Number,
    child : Object,
  })

  const emit = defineEmits(['giveMeAllowance'])

  const giveMeAllowance = function () {
    emit('giveMeAllowance', props.child)
  }

</script>

<style scoped>

</style>