<template>
  <div>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="goUpdate(balance.name)">UpdateBalance</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

defineProps({
  balance : Object,
})

const goUpdate = function (name) {
  //updateView로 이동
  router.push({name: 'update', params: {name: name} })
}

</script>

<style scoped>

</style>