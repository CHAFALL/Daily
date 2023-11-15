<template>
  <div>
    <h1>Signup</h1>
  </div>
  <form @submit.prevent="signUp">
    <input type="text" v-model.trim="username">
    <input type="password" v-model.trim="password1">
    <input type="password" v-model.trim="password2">
    <input type="submit">
  </form>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  // 보통 전달하는 인자를 payload로 많이 씀
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}


</script>

<style>

</style>
