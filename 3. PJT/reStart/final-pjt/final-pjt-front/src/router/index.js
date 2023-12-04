import { createRouter, createWebHistory } from 'vue-router'
import EasterEggView from '@/views/EasterEggView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import RecommendedView from '@/views/RecommendedView.vue'
import CommunityListView from '@/views/CommunityListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import UserDetailView from '@/views/UserDetailView.vue'
import MovieGenreView from '@/views/MovieGenreView.vue'
import ActorView from '@/views/ActorView.vue'
import { useUserStore } from '@/stores/user'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: (to, from) => {
        const userStore = useUserStore()
        if (userStore.isLogin) {
          window.alert('이미 로그인 상태입니다.')
          return { name : 'movies'}
        }
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView,
      beforeEnter: (to, from) => {
        const userStore = useUserStore()
        if (userStore.isLogin) {
          window.alert('이미 로그인 상태입니다.')
          return { name : 'movies'}
        }
      }
    },
    {
      path: '/',
      name: 'movies',
      component: MovieListView
    },
    {
      path: '/movies/:id',
      name: 'movie',
      component: MovieDetailView
    },
    {
      path: '/recommended',
      name: 'recommended',
      component: RecommendedView,
      beforeEnter: (to, from) => {
        const userStore = useUserStore()
        if (!userStore.isLogin) {
          window.alert('로그인이 필요합니다.')
          return { name: 'login'}
        }
      }
    },
    {
      path: '/articles',
      name: 'articles',
      component: CommunityListView,
      beforeEnter: (to, from) => {
        const userStore = useUserStore()
        if (!userStore.isLogin) {
          window.alert('로그인이 필요합니다.')
          return { name: 'login'}
        }
      }
    },
    {
      path: '/articles/create',
      name: 'create',
      component: ArticleCreateView,
      beforeEnter: (to, from) => {
        const userStore = useUserStore()
        if (!userStore.isLogin) {
          window.alert('로그인이 필요합니다.')
          return { name: 'login'}
        }
      }
    },
    {
      path: '/articles/:id',
      name: 'article',
      component: ArticleDetailView,
      beforeEnter: (to, from) => {
        const userStore = useUserStore()
        if (!userStore.isLogin) {
          window.alert('로그인이 필요합니다.')
          return { name: 'login'}
        }
      }
    },
    {
      path: '/articles/:id/update',
      name: 'update',
      component: ArticleUpdateView,
      beforeEnter: (to, from) => {
        const userStore = useUserStore()
        if (!userStore.isLogin) {
          window.alert('로그인이 필요합니다.')
          return { name: 'login'}
        }
      }
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: UserDetailView
    },
    {
      path: '/genres/:id',
      name: 'genre',
      component: MovieGenreView
    },
    {
      path: '/actor/:id',
      name: 'actor',
      component: ActorView
    },
    {
      path: '/meow',
      name: 'easteregg',
      component: EasterEggView,
    },
  ]
})

export default router
