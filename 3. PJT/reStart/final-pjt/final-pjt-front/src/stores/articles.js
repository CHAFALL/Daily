import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref([]) // 게시글 목록 저장하는 변수

  // 게시글 목록 가져와서 저장하는 함수
  const getArticles = function (token) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/community/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then(res => {
        articles.value = res.data.reverse()
      })
      .catch(err => console.log(err))
  }



  return { API_URL, articles, getArticles }
})