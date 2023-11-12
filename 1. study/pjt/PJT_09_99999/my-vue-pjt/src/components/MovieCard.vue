<template>
  <div @click="goDetail">
    <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="#">
    {{ movie.title }}
    <hr>
    {{ movie.overview }}
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps(['movie'])

const router = useRouter()

const goDetail = () => {
  router.push(`/${props.movie.id}`)
}
</script>

<style scoped>

</style>