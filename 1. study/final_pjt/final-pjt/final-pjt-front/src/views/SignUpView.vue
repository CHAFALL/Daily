<template>
  <div style="background-color: rgba(51, 51, 51, 0.8); text-align: center; color: white;">
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      <v-text-field v-model.trim="username" label="Username" class="custom-text-field"></v-text-field>
      <v-text-field v-model.trim="password1" label="Password" type="password" class="custom-text-field"></v-text-field>
      <v-text-field v-model.trim="password2" label="Confirm Password" type="password" class="custom-text-field"></v-text-field>
      <v-btn type="submit" class="custom-signup-btn">Sign Up</v-btn>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

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
.custom-text-field {
  text-align: center;
  height: 30px; /* Adjust the height as needed */
  font-size: 14px; /* Adjust the font size as needed */
  margin-bottom: 20px;
  padding: 10px;
}

.custom-signup-btn {
  margin-top: 25px; /* Adjust the margin-top as needed */
}
</style>