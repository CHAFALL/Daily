import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then((res) => {
      console.log(res)
      articles.value = res.data
    })
    
  }

  const createArticles = function ({title, content}){
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content,
      }
    })
      .then((res) => {
        console.log(res)
      })
    
  }



  return { articles, getArticles, createArticles }
})
