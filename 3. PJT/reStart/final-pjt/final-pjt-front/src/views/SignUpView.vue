<template>
  <div class="container">
    <h1 class="navbar" style="font-size: 45px;">Sign up</h1>
    <form @submit.prevent="signUp" autocomplete="off" class="form">
      <input type="text" id="username" placeholder="username" v-model="username"><br>
      <input type="email" id="email" placeholder="email" v-model="email"><br>
      <input type="password" id="password1" placeholder="password1" v-model="password1"><br>
      <input type="password" id="password2" placeholder="password2" v-model="password2"><br>
      <button style="margin-top: 30px;">회원 가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
const store = useUserStore()

const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const signUp = function () {
  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
 .container{
  border: 1px solid lightgrey;
  position: absolute;
  display: flex;
  flex-direction: column;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  width: 400px;
  height: 500px; 
  border-radius: 3%;
  box-shadow: 0 2px 8px 2px rgba(0,0,0,0.2);
 }


 form input {
  background: #eee;
  padding: 16px;
  margin: 8px 0;
  width: 250px;
  border: 0;
  outline: none;
  border-radius: 20px;
  box-shadow: inset 7px 2px 10px #babebc, inset -5px -5px 12px #fff;
}

button {
  border-radius: 20px;
  border: none;
  outline: none;
  font-size: 12px;
  font-weight: bold;
  padding: 15px 45px;
  margin: 14px;
  letter-spacing: 1px;
  text-transform: uppercase;
  cursor: pointer;
  transition: transform 80ms ease-in;
}

</style>