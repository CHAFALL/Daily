<template>
  <body>
    
    <v-app style="background-color: black; font-size: 18px;">
      <v-app-bar style="background-color: lightslategray; padding: 5px;">
        <div class="nav-links">
          <RouterLink class="nav-link" :to="{ name: 'MovieView' }">홈</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'ReviewView' }">커뮤니티</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'LaterView' }">찜</RouterLink>
        </div>
          <v-spacer></v-spacer>
          <!-- 모달 구현 방법 -->
          <div v-if="!store.isLogin">
          <v-btn  class="modal"
          @click="openDialog('login')" style="color: white;">
            로그인
          </v-btn>
          <v-btn  class="modal"
          @click="openDialog('signup')" style="color: white;">
            회원가입
          </v-btn>
        </div>
        <div v-else>
          <v-btn  class="modal"
          @click="logOut" style="color: white;">
            로그아웃
          </v-btn>
        </div>

          <v-dialog
          max-width="800px"
          v-model="dialogOpen"
          >
          <LogInView
            v-if="dialogType === 'login'" 
            @close-dialog="closeDialog"
          />
          <SignUpView
            v-if="dialogType === 'signup'" 
            @close-dialog="closeDialog"
          />
        </v-dialog>
        
      </v-app-bar>
      <RouterView />
    </v-app>

</body>
</template>

<script setup>
import { ref } from 'vue'
import  LogInView  from '@/views/LogInView.vue';
import SignUpView from '@/views/SignUpView.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

const logOut = function () {
  store.logOut()
}

const dialogType = ref('')
const dialogOpen = ref(false)

const closeDialog = () => {
  dialogOpen.value = false

}

const openDialog = (type) => {
  dialogType.value = type
  dialogOpen.value = true
}

</script>

<style>
body {
  font-family: 'Arial', sans-serif;
}

.back {
  background-color: black;
  padding: 10px;
}

nav {
  display: flex;
  justify-content: space-between;
}

.left-items {
  display: flex;
}

.right-items {
  display: flex;
}


.nav-links {
  display: flex;
  align-items: center;
}


.nav-link {
  color: white;
  margin-right: 10px;
  text-decoration: none;
  font-size: 20px;
  padding-left: 10px;
}

.modal {
  font-size: 20px;
  width: 100px;
}

</style>