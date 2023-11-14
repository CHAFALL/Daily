<template>
  <div>
    <h2>수정 페이지</h2>
    <p>이름 : {{ detailInfo.name }}</p>
    <p>잔고 : {{ detailInfo.balance }}</p>
    <button @click="store.updateBalance(detailInfo.name)">+</button>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useBalanceStore } from '@/stores/balance';
const store = useBalanceStore()
const route = useRoute()

//console.log(store.detailInfo(route.params.name))
const detailInfo = store.detailInfo(route.params.name)
</script>

<style scoped>

</style>