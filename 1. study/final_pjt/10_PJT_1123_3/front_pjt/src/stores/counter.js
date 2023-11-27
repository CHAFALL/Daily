import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  
  const movies = ref([])
  const reviews = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const genres = ref([])
  const userInfo = ref('')

  

  // 로그인 여부 확인 만들기
  const isLogin = computed(()=> {
    if (token.value===null){
      return false
    } else {
      return true
    }
  })


  // DRF에 movie 조회 요청을 보내는 action
  const getMovies = function() {
    axios({
      method: 'get',
      // 여기 끝에 슬래시 빼먹지 말기!!
      url: `${API_URL}/api/v1/movies/`,
      headers: {                                  // 토큰 인증
        Authorization: `Token ${token.value}`     
      }
    })
      .then((res)=>{
        
        const currentUserID = userInfo.value.user_info.id
        // 현재 사용자의 ID가 uninterest_users 배열에 포함되지 않은 영화만 필터링합니다.
        const filteredMovies = res.data.filter(movie => !movie.uninterest_users.includes(currentUserID));

        // 필터링된 영화 목록을 movies.value에 할당합니다.
        movies.value = filteredMovies;
       
      })
      .catch((err)=>{
        console.log(err)
      })
  }


  // DRF에 review 조회 요청을 보내는 action
  const getReviews = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community/review/`,
      headers: {                                  //
        Authorization: `Token ${token.value}`     
      }
    })
      .then((res) =>{
        // console.log(res)
        reviews.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  
  // 장르 가져오기
  const getGenre = function() {
    axios({
      method: 'get',
      // 여기 끝에 슬래시 빼먹지 말기!!
      url: `${API_URL}/api/v1/get_genres/`,
      headers: {                                  // 토큰 인증
        Authorization: `Token ${token.value}`     
      }
    })
      .then((res)=>{
        genres.value = res.data
      })
      .catch((err)=>{
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
      // 회원가입 성공 후 자동으로 로그인까지 진행하기
      const password = password1
      logIn({username, password})
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  // 로그인
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
    // 토큰을 그냥 날려버리면 안된다.(날려버리면 다른 페이지 이동을 비인증 상태로 이동하게 되어서 걸림-> 저장하자! )
    .then((res)=>{
      console.log(res.data)
      token.value = res.data.key
      // 로그인 했으면 홈으로
      // router.push({name:'MovieView'})
      router.go()
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  // 로그아웃
  const logOut = function () {
    // 1. 사용자 입력 데이터를 받아
    // 2. 서버로 로그인 요청 및 응답 받은 토큰 저장
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {                                  // 토큰 인증
        Authorization: `Token ${token.value}`     
      }
    })
    .then((res)=>{
      token.value = null
  
      router.push({name:'MovieView'})
    })
    .catch((err)=>{
     
    })
  }


  const getUserInfo = function() {
    axios({
      method: 'get',
      // 여기 끝에 슬래시 빼먹지 말기!!
      url: `${API_URL}/api/v1/userinfo/`,
      headers: {                                  // 토큰 인증
        Authorization: `Token ${token.value}`     
      }
    })
      .then((res)=>{
        // console.log(res.data)
        userInfo.value = res.data
  
      })
      .catch((err)=>{
        console.log(err)
      })
  }
  
  return { movies, API_URL, getMovies, signUp, logIn, logOut, token, isLogin, getReviews, reviews, genres, getGenre, getUserInfo, userInfo}
}, { persist: true })

