<template>
  <div class="container">
    <h1 class="navbar" style="font-size: 45px;">Login</h1>
    <div class="button-container">
      <div class="brandimg">
        <img src="https://upload.wikimedia.org/wikipedia/ko/thumb/9/9e/%ED%8A%B8%EC%9C%84%ED%84%B0_%EB%A1%9C%EA%B3%A0_%282012%29.svg/172px-%ED%8A%B8%EC%9C%84%ED%84%B0_%EB%A1%9C%EA%B3%A0_%282012%29.svg.png?20151031083522" alt="트위터">
        <img src="@/assets/facebook_png_640.png" style="width: 80px;" alt="페이스북">
        <img src="https://w7.pngwing.com/pngs/866/916/png-transparent-logo-computer-icons-instagram-instagram-application-logo-text-trademark-magenta-thumbnail.png" alt="인스타그램">
      </div>
      <form @submit.prevent="logIn" autocomplete="off">
        <input type="text" id="username" placeholder="username" v-model="username"><br>
        <input type="password" id="password" placeholder="password" v-model="password"><br>
        <div class="button-group">
          <button>로그인</button>
          <RouterLink :to="{name:'signup'}">
            <button>회원가입</button>
          </RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
const store = useUserStore()

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

  h1{
    margin-bottom: 50px;
  }

  img{
    width: 50px;
  }

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
  padding-bottom: 30px;
 }

 form input {
  background: #eee;
  padding: 16px;
  margin-top: 20px;
  width: 85%;
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

.button-group{
  margin-top: 50px;
  display: flex;
  justify-content: center;
}

.brandimg {
    cursor: pointer;
    margin-top: px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .brandimg img {
    width: 40px;
    height: auto;
    object-fit: contain;
    margin: 0 10px;
  }

</style>