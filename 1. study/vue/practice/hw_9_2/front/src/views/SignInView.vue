<template>
  <div>
    <h1>signIn</h1>
    <form @submit.prevent="signIn">
      <input type="text" v-model.trim="username">
      <input type="password" v-model.trim="password">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const username = ref(null)
const password = ref(null)

const signIn = function () {
  const payload = {
    username : username.value,
    password : password.value,
  }
  store.signIn(payload)
}


</script>

<style>

</style>
