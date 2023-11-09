import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'


const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from)=> {
        console.log(to)
        console.log(from)
      }
    },
    // 다른 곳에서 userview로 진입할 때마다 실행될 라우터 가드
    // 어떤 사용자가 프로필(user)로 들어올 때마다 확인해야 될 것이 있다면 사용

    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter:(to, from)=>{
        if (isAuthenticated === true) {
          console.log('이미 로그인되어 있습니다.')
          return { name:'home' }
        }
      }
    },
  ]
})

// to는 내가 이동할 route 객체이고 from는 내가 현재 위치한 route 객체
// 우리가 직접 호출하는 것이 아닌 특정 상황(다른 곳으로 이동하기 직전.)마다 자동으로.
// 세션 같은 것 관리 할 때 쓰이겠지~
// router.beforeEach((to, from)=>{
//   // console.log(to)
//   // console.log(from)
//   const isAuthenticated = false
//   // 예외 상황도 생각해야지!
//   if (!isAuthenticated && to.name !=='login') {
//     console.log('로그인이 필요합니다.')
//     return { name:'login' }
//   }
// })

export default router
