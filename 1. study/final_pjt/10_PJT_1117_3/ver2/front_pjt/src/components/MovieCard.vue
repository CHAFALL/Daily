<template>
  <div @click="goDetail">
    <h5>{{ movie.id }}</h5>
    <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="#">

    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()

const props = defineProps({
  movie:Object,
})

const goDetail = () => {
  router.push(`movies/${props.movie.id}`)
}
</script>
