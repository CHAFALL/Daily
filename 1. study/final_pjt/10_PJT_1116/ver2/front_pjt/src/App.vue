<template>
  <header>
    <nav>
      <RouterLink :to="{name : 'MovieView'}" >Movies</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
