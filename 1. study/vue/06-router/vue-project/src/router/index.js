import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'


const isAuthenticated = true


//guard도 이 router 객체 안에 있다.
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // 해당 라우트가 실행이 되었을 때 HomeView라고 하는 컴포넌트를 보여주겠다.

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
      beforeEnter: (to, from) => {
        console.log(to)
        console.log(from)
      }
    },

    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated ===true){
          console.log('이미 로그인되어 있습니다.')
          return { name:'home' }
        }
      }
    },
  ]
})

// router.beforeEach((to, from) => {
//   console.log(to)
//   console.log(from)
// })


// 전역 가드
// router.beforeEach((to, from)=>{
//   const isAuthenticated = false

//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return { name: 'login' }
//   }
// })

export default router
