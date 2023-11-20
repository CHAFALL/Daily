<!-- <template>

    <div >

        <h5>{{ movie.id }}</h5>
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="#" @click="goDetail">
        <hr>

    </div>

</template> -->

<!-- 2 -->
<template> 

  <v-card @click="goDetail">
    <v-card-title style="width: 200px;">
      <v-img
        :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
        alt="#"
        style="width: 100%; height: 100%; object-fit: cover;"
      ></v-img>
    </v-card-title>
    <v-divider></v-divider>
  </v-card>

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


<style scoped>
 

</style>