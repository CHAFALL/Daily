import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const movies = ref([])  // 영화 목록 저장하는 변수
  const genres = ref([])

  let allDataLoaded = false
  const pageSize = 50
  const scrollThreshold = 95

  // 영화 목록 가져와서 저장하는 함수
  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
    })
      .then(res => {
        if (res.data.length < pageSize) {
          allDataLoaded = true
        }
        res.data.forEach(movie => {
          if (!movies.value.find(m => m.id === movie.id)) {
            movies.value.push(movie)
          }
        })
        return movies.value
      })
      .catch(err => {
        console.log(err)
        return []
      })
  }

  function loadMoreMovies() {
    if (allDataLoaded) return
    getMovies()
  }

  const getGenres = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/genres/`
    })
      .then(res => {
        genres.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { API_URL, getMovies, movies, loadMoreMovies, scrollThreshold, getGenres, genres }
})