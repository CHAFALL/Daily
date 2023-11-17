import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  // 로그인 가능 여부 만들기
  const isLogin = computed(()=> {
    if (token.value===null){
      return false
    } else {
      return true
    }
  })


  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {                                  //
        Authorization: `Token ${token.value}`     
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function ({ username, password1, password2 }) {
    // 1. 사용자 입력 데이터를 받아
    // 2. 서버로 회원가입 요청을 보냄 
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data:{
        username,
        password1,
        password2
      }
    })
    .then((res)=>{
      console.log(res)
    })
    .catch((err)=>{
      console.log(err)
    })
  }


  const logIn = function ({ username, password }) {
    // 1. 사용자 입력 데이터를 받아
    // 2. 서버로 로그인 요청 및 응답 받은 토큰 저장
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data:{
        username,
        password,
      }
    })
    // 토큰을 그냥 날려먹으면 안된다.(날려버리면 다른 페이지 이동을 비인증 상태로 이동하게 되어서 걸림-> 저장하자! )
    .then((res)=>{
      console.log(res.data)
      token.value = res.data.key
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  // token 리턴 까먹지 말기!
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })


// 회원가입을 중앙 저장소에 두는 이유 : 중앙 저장소에서 getArticles라고 하는 전체 게시글 요청을 보내고 있는데, 회원가입하고 회원가입 이후, 로그인하고 토큰 받고 하려면 결국 여기에 있는 토큰 데이터를 최종적으로 저장에 관여하는 함수가 될 것이므로???

// 다른 것보다도 더욱 더 로그인이 중앙 저장소에 있어야하는 이유: 로그인은 요청이 갔다가 오고나서 로그인 처리를 하려면, 로그인 중에 토큰을 발급 받음. 그 토큰을 이 중앙 저장소에 저장을 해야 Good, 그래야 store에 있는 토큰을 추가하거나 삭제하거나 할 수 o 

// 토큰을 중앙 저장소에 두는 이유: 하위에 있는 모든 컴포넌트가 인증이 필요한 요청을 할 때 토큰을 참조해야 해서, 각자 들고 있는 것 보다 중앙 저장소에 두는 것이 훨씬 good(모두가 참조 가능하도록)