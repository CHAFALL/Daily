<template>
  <div>
    <MainPage/>
    <RouterLink :to="{name:'some'}">Some</RouterLink> |
    <RouterLink :to="{name:'other'}">Other</RouterLink> |
    <RouterLink :to="{name:'students'}">Students</RouterLink> 
  </div>
  <RouterView/>
</template>

<script setup>
  import MainPage from '@/components/MainPage.vue'
</script>

<style scoped>

</style>