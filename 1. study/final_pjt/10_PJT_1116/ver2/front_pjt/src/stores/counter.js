import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getMovies = function() {
    axios({
      method: 'get',
      // 여기 끝에 슬래시 빼먹지 말기!!
      url: `${API_URL}/api/v1/movies/`,
    })
      .then((res)=>{
        console.log(res)
        movies.value = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
  }
  
  
  
  return { movies, API_URL, getMovies }
}, { persist: true })
