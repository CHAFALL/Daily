<template>
  <div class="preferedarticle">
    <p>
      <span @click="router.push({name: 'article', params:{id: article.id}})">
        {{ article.title }}
      </span>
       - 
      <span @click="router.push({name: 'profile', params:{username: article.user.username}})">
        {{ article.user.username }}
      </span>
    </p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
  article: Object
})
</script>

<style scoped>

</style>
