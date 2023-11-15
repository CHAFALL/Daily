import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
// import { createPinia } from 'pinia'
// import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// const pinia = createPinia()
// pinia.use(piniaPluginPersistedstate)
export const useArticleStore = defineStore('article', () => {


  
  const router = useRouter()
  const articles = ref([])
  const token = ref(null)

  const isLogin = computed(()=>{
    if (token.value === null){
      return false
    } else {
      return true
    }
  })


  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function({username, password1, password2}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username, password1, password2
      }
    })
      .then((res)=>{
        // console.log(res)
        const password = password1
        signIn({username, password})
      })
      .catch((err)=>{
        console.log(err)
      })
  }

  const signIn = function ({username, password}){
    
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    })
    .then((res)=>{
      console.log(res.data)
      token.value = res.data.key
      router.push({name:'home'})
    })
    .catch((err)=>{
      console.log(err)
    })
  }


  return { articles, getArticles, createArticle, signUp, signIn, isLogin }
},{ persist: true })
