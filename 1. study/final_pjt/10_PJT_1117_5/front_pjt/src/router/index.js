import { createRouter, createWebHistory } from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ReviewView from '@/views/ReviewView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ReviewCreateView from '@/views/ReviewCreateView.vue'





const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MovieView',
      component: MovieView
    },
    {
      path: '/movies/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/reviews',
      name: 'ReviewView',
      component: ReviewView
    },
    {
      path: '/reviews/:id',
      name: 'ReviewDetailView',
      component: ReviewDetailView
    },
    {
      path: '/reviewsCreate',
      name: 'ReviewCreateView',
      component: ReviewCreateView
    }
  ]
})

// 나중에 열자!!
// import { useCounterStore } from '@/stores/counter'

// router.beforeEach((to, from)=>{
//   // 안 쪽에서 해주는 것 보소.
//   const store = useCounterStore()
//   if (to.name==='ArticleView' && !store.isLogin) {
//     window.alert('로그인이 필요합니다.')
//     return {name: 'LogInView'}
//   }

//   if ((to.name==='SignUpView' || to.name==='LogInView') && (store.isLogin)) {
//     window.alert(' 이미 로그인했습니다.')
//     return {name: 'ArticleView'}
//   }
// })

export default router
