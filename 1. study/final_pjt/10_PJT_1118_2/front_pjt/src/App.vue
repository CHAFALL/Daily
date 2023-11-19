<template>
  <header>
    <nav>
      <RouterLink :to="{name : 'MovieView'}" >Movies</RouterLink> |
      <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink> |
      <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink> |
      <RouterLink :to="{ name: 'ReviewView' }">Review</RouterLink> |
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
