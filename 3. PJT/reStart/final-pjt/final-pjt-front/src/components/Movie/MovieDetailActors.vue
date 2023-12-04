<template>
<div class="carousel-container">
  <div class="carousel">
    <MovieDetailActorsItem 
      v-for="actor in actors"
      :key="actor.id"
      :actor="actor"
    />
  </div>
</div>

</template>

<script setup>
import MovieDetailActorsItem from '@/components/Movie/MovieDetailActorsItem.vue'
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const props = defineProps({
  movieId: Number,
})

const actors = ref(null)

const fetchActorData = function () {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/movies/${props.movieId}/actors/`,
  })
    .then(res => {
      actors.value = res.data
    })
    .catch(err => console.log(err))
}

onMounted(() => {
  fetchActorData()
})

watch(() => props.movieId, () => {
  fetchActorData()
})
</script>

<style scoped>
.carousel-container {
  overflow-x: scroll;
  white-space: nowrap;
  scrollbar-width: thin;
  scrollbar-color: #888 transparent;
}

.carousel {
  display: flex;
  gap: 16px;
  padding-bottom: 16px;
}
</style>