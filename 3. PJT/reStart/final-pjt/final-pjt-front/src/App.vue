<template>
  <header class="container" style="margin-top: ;">
    <nav class="navbar">
      <div class="navigation-bar">
        <img src="@/assets/logo.png" class="logo" alt="" @click="router.push({name: 'easteregg'})">
        <div class="nav-links">
          <RouterLink :to="{name:'movies'}">Movies</RouterLink>
          <RouterLink :to="{name:'recommended'}">Recommended</RouterLink>
          <RouterLink :to="{name:'articles'}">Community</RouterLink>
        </div>
      </div>

      <div class="dropdown">
        <img src="https://toppng.com/uploads/preview/roger-berry-avatar-placeholder-11562991561rbrfzlng6h.png" style="width: 50px; height: 50px;" class="dropbtn">
        <div class="dropdown-content" v-if="userStore.isLogin">
          <p>{{ userStore.currentUser }}</p>
          <RouterLink :to="{name: 'profile', params:{username: userStore.user}}">My profile</RouterLink>
          <p @click="userStore.logOut" style="cursor: pointer;">Logout</p>
        </div>
        <div class="dropdown-content" v-else>
          <RouterLink :to="{name:'signup'}">Signup</RouterLink>
          <RouterLink :to="{name:'login'}">Login</RouterLink>
        </div>
      </div>
    </nav>
  </header>
  <RouterView/>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
const router = useRouter()
</script>

<style scoped>
.logo {
  margin-left: 10px;
  width: 70px;
  height: auto;
}
.dropbtn{
  margin-top: 5px;
}


.container{
  position: sticky;
  display: flex;
  align-items: center;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2);
  top: 0;
  z-index: 50;

}

header {
  line-height: 1.5;
  max-height: 100vh;
  background-color: #f4f4f5;
  padding: 5px 0;
  width:100%;
}

nav {
  display: flex;
  justify-content: space-between;
  width: 100%;
  height : 70px;
  font-size: 20px;
  text-align: center;
  font-size: 25px;
}

.navigation-bar{
  display: flex;
  flex-direction: row;
  align-items: center;
}

.nav-links a.router-link-exact-active {
  color: lightgrey;
  font-weight: bold;
}

.nav-links a {
  display: inline-block;
  padding: 15px 20px;
  color: #343a40;
  text-decoration: none;
  transition: color 0.3s ease;
  border-radius: 50px;
}

.nav-links a:hover {
  color: #fff;
  background-color: lightgrey;
  border-radius: 50px;
  padding: 8px 18px;
  
}

.dropdown {
  position: relative;
  display: inline-block;
  align-self: center;
  width: 50px;
  margin-right: 30px;
  margin-top: 10px;
  cursor: pointer;
}

.dropdown-content {
  display: none;
  position: absolute;
  right: 0;
  background-color: #f1f1f1;
  min-width: 100px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 5;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #3e8e41;
  }
</style>

<style>
  .navbar{
    font-family: 'Indie Flower', cursive;
    text-align: center;
  }

  .next-prev{
  border: 1px solid lightgrey;
  color: black;
  width: 120px;
  height: 40px;
  background-color: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
}

.next-prev:hover {
  border: 2px solid lightgrey;
  background-color: rgb(238, 238, 238);
}

</style>