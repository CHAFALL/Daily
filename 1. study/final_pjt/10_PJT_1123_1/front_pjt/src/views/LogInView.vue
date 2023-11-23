<template>
  <div style="background-color: rgba(51, 51, 51, 0.8); text-align: center; color: white;">
    <h1>Login</h1>
    <form @submit.prevent="logIn" style="text-align: center;">
      <v-text-field v-model.trim="username" label="Username" class="custom-text-field"></v-text-field>
      <v-text-field v-model.trim="password" label="Password" class="custom-text-field" type="password"></v-text-field>
      <v-btn type="submit">LogIn</v-btn>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}
</script>

<style scoped>
.custom-text-field {
  text-align: center;
  height: 30px; /* Adjust the height as needed */
  font-size: 14px; /* Adjust the font size as needed */
  margin-bottom: 50px;
  padding: 50px;
  background-color: rgba(68, 68, 68, 0.7); /* Darker background color with 70% opacity */
  color: white; /* Text color */
}
</style>