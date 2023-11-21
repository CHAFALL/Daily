<template>

<div style="color: white;">
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      <v-text-field v-model.trim="username" label="Username" ></v-text-field>
      <v-text-field v-model.trim="password1" label="Password" type="password" ></v-text-field>
      <v-text-field v-model.trim="password2" label="Confirm Password" type="password" ></v-text-field>
      <v-btn type="submit">Sign Up</v-btn>
    </form>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import {useCounterStore} from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style scoped>

</style>
