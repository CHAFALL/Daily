<template>
  <h1>데이터 수정 페이지</h1>
  <p>이름: {{ userName }}</p>
  <p>잔고:{{ userBalance.balance }}</p>
  <button @click="store.updateBalance(userBalance)">+</button>
  
  
</template>

<script setup>
import {useRoute} from 'vue-router'
import { useBalanceStore } from '@/stores/balance'
const route = useRoute()
const store = useBalanceStore()

const userName = route.params.name
const userBalance = store.getters(userName)

</script>

<style scoped>

</style>