<template>
  <body>
    
    <v-app style="background-color: black; font-size: 30px;">
      <v-app-bar style="background-color: lightslategray;">
        <header>
          <RouterLink class="nav-link" :to="{ name: 'MovieView' }">Movies</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'ReviewView' }">Review</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'SignUpView' }">SignUpView</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'LaterView' }">LaterView</RouterLink>
          
          <!-- 모달 구현 방법 -->
          <v-btn
          @click="openDialog('login')" style="color: white;">
            로그인실험 모달
          </v-btn>

          <v-dialog
          max-width="800px"
          v-model="dialogOpen"
          >
          
          <LogInView
            v-if="dialogType === 'login'" 
            @close-dialog="closeDialog"
          />
        </v-dialog>
        </header>
      </v-app-bar>
      <RouterView />
    </v-app>

</body>
</template>

<script setup>
import { ref } from 'vue'
import  LogInView  from '@/views/LogInView.vue';
import SignUpView from '@/views/SignUpView.vue';

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

.nav-link {
  color: white;
  margin-right: 10px;
  text-decoration: none;
}
</style>