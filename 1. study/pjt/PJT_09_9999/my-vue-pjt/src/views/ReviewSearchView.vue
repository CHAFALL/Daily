<template>
  <div>
    <h1>ReviewSearchView</h1>
    <form @submit.prevent="searchMovie">
      <input type="text" placeholder="영화제목을 검색해보세요." v-model="inputText">
      <button>검색</button>
    </form>
    
    <div v-for="video in videos" :key="video.id.videoId">
      <div @click="toggleVideoPlay(video)">
        <div v-if="isVideoPlaying(video)">
          <iframe
            id="ytplayer" 
            type="text/html" 
            width="720" 
            height="405" 
            :src="`https://www.youtube.com/embed/${video.id.videoId}`" frameborder="0" 
            allowfullscreen
          ></iframe>
        </div>
        <div v-else>
          <img :src="video.snippet.thumbnails.medium.url" alt="#">
          {{ video.snippet.title }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const inputText = ref('')
const videos = ref([])
const youtubeUrl = 'https://www.googleapis.com/youtube/v3/search'
const apiKey = 'AIzaSyDKuyw9F38_yga3L_eess7RaWfYfSWatx8'

const playingVideo = ref(null)

const toggleVideoPlay = function (video) {
  playingVideo.value = playingVideo.value === video ? null : video
}

const isVideoPlaying = function (video) {
  return playingVideo.value === video
}

const searchMovie = function() {
  axios.get(youtubeUrl,{
    params: {
      q: inputText.value,
      part: 'snippet',
      type: 'video',
      key: apiKey,
    }
  })
    .then((res) => {
      console.log(res.data.items)
      videos.value = res.data.items
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>
