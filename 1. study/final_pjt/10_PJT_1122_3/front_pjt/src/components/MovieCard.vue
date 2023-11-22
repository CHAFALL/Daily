
<template> 

  <v-card @click="goDetail" style="background-color: black;" >
    <v-card-title class="hover" style="background-color: black; width: 420px;">
      <v-img 
        :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
        alt="#"
        style="width: 100%; height: 500px; object-fit: cover;"
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
 
.hover:hover {
  transform: scale(1.1);
  transition: 0.2s;
}
</style>