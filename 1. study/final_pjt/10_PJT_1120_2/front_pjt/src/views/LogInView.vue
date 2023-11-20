<template>
  <div style="color:white">
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <v-text-field v-model.trim="username" label="Username" class="custom-text-field" ></v-text-field>
      <v-text-field v-model.trim="password" label="Password" class="custom-text-field" type="password"></v-text-field>
      <v-btn type="submit">LogIn</v-btn>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useCounterStore} from '@/stores/counter'

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
    width: 200px; /* Adjust the width as needed */
    height: 30px; /* Adjust the height as needed */
    font-size: 14px; /* Adjust the font size as needed */
    margin-bottom: 50px;
  }
</style>
