<template>
  <div>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="goUpdate(balance)">updateBalance</button>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'

defineProps({
  balance: Object
})

const router = useRouter()
const goUpdate = function (balance) {
  router.push({name:'update',params: { name : balance.name} })
}

</script>

<style scoped>

</style>