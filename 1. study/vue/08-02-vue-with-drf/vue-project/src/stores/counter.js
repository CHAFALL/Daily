import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  //computed로 하는 이유, 매번 바뀌는 것이 아니라 토큰의 값이 바뀔 때만 값이 바뀌면 되므로
  const isLogin = computed(()=>{
    if (token.value === null){
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
      headers: {
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

  const signUp = function (payload) {
    // 이거 해주는 이유: 아래에 단축속성을 쓰려고 하는데 payload.xxx로 되어있으면 써먹을 수 없어서.
    const {username, password1, password2} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
      }
      
    })
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=>{
        console.log(err)
      })
  }   

  // login은 signup보다 처리할 것이 하나 더 있음.
  // 응답에 있는 토큰을 받아서 store에 있는 토큰에다가 저장해줘야 함.

  const logIn = function (payload) {

    const {username, password} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      }
      
    })
      .then((res)=>{
        console.log(res.data)
        token.value = res.data.key
      })
      .catch((err)=>{
        console.log(err)
      })
  }


  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin}
}, { persist: true })


// 중앙저장소에서 getArticles라고 하는 전체 게시글 요청을 보내고 있다.
// 회원가입도 결국 회원가입 이후하고 로그인하고 토큰 받고 하려면 여기에 있는 토큰 데이터를 최종적으로 저장에 관여하는 함수가 될 것이므로? 여기에 작성해보자!

// 로그인도 store에 있어야 한다. 로그인은 요청이 갔다가 오고나서 로그인 처리를 하려면 토큰이 필요. (그래서 토큰을 발급받음) (이 토큰을 중앙저장소에 저장해야 해서 다른 어떠한 함수보다 반드시 이 store에 있어야 한다.) 그래야 store에 있는 토큰의 값을 추가하거나 삭제 가능.

// 토큰을 중앙저장소에 두는 이유는? (하위에 있는) 모든 component가 인증에 필요한 요청을 할 때 토큰을 참조해야하는 데 토큰을 각자 들고 있는 것이 아니라 중앙저장소에 두면 간편하게 참조 가능