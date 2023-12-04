import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null) // 현재 로그인 한 사용자의 토큰 저장하는 변수
  const user = ref(null)  // 현재 로그인 한 사용자의 아이디(username)를 저장하는 변수
  const isLogin = computed(() => {  // 현재 로그인 여부를 판단하는 변수
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()

  // 회원 가입 함수
  const signUp = function ({username, password1, password2}) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: { username, password1, password2 }
    })
      .then(res => {
        const password = password1
        logIn({username, password})
      })
      .catch(err => {
        if (password1 !== password2) {
          window.alert('비밀번호가 서로 일치하지 않습니다.')
        }
        console.log(err)
      })
  }

  // 로그인 함수
  const logIn = function({ username, password}) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: { username, password }
    })
      .then(res => {
        // console.log(res.data)
        token.value = res.data.key
        user.value = username
        router.push({name: 'movies'})
      })
      .catch(err => {
        window.alert('로그인 정보가 잘못되었습니다.')
        console.log(err)
      })
  }

  // 로그아웃 함수
  const logOut = function() {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then(res => {
        token.value = null
        user.value = null
        router.push({name: 'login'})
      })
  }
  

  return { API_URL, signUp, logIn, token, isLogin, logOut, user }
}, { persist:true } )
