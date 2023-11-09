<template>
  <div class="business-card-detail">
    <h3>이름: {{ businessCard.name }}</h3>
    <p>직함: {{ businessCard.title }}</p>
    <button @click="deleteCardFunc(businessCard)">명함삭제</button>
  </div>
</template>

<script setup>
  defineProps({
    businessCard : Object,
  })

  const emit = defineEmits(['deleteCardEvent'])
  // 이렇게도 인자 보낼 수 있음
  const deleteCardFunc = function (targetCard) {
    emit('deleteCardEvent', targetCard)
  }

</script>


  

<style scoped>
  .business-card-detail{
    width: 40%;
    border: 1px solid lightgray;
    background-color: whitesmoke;
    padding: 20px;
    margin: 20px;
  }
</style>