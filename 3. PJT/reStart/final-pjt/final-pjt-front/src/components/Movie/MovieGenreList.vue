<template>
  <div>
    <div v-if="genres">
      <button
       class="genre-button"
       v-for="genre in genres"
       :key="genre.id"
       @click="router.push({name: 'genre', params:{id: genre.id}})"
      >
        {{ genre.name }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
const router = useRouter()

const genres = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/api/v1/movies/genres/`
  })
    .then(res => {
      genres.value = res.data
    })
    .catch(err => console.log(err))
})
</script>

<style scoped>
.genre-button {
  background-color: #757575;
  border: none;
  color: white;
  padding: 5px 15px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  height: 50px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
  border-radius: 25px;
  transition: 0.3s ease-in;
}

.genre-button:hover {
  background-color: #BDBDBD;
  color: black;
  /* transform: scale(0.8, 1, 1.3); */
  transform: scale(1.2);
}
</style>
