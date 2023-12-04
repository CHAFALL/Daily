<template>
  <div>
    <img :src="imgUrl + actor.profile_path" alt="No image" @click="router.push({name: 'actor', params:{id: actor.id}})">
    <p>{{ actor.name }}</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
  actor: Object,
})

const imgUrl = "https://image.tmdb.org/t/p/w185"
// w45 / w185 / h632 / original
</script>

<style scoped>

</style>