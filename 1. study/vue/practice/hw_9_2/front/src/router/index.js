import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInView from '@/views/SignInView.vue'
import { useArticleStore } from '@/stores/articles'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
      beforeEnter: (to, from)=> {
        const store = useArticleStore()
        console.log(to)
        console.log(from)
        // if (!store.isLogin) {
        //     return {name: 'home'}
        //   }
        if (store.token && to.name === 'SignInView' || to.name === 'SignUpView' ) {
          return {name : 'home'}
        }
      }
    },
    {
      path: '/signin',
      name: 'SignInView',
      component: SignInView,
      beforeEnter: (to, from)=> {
        const store = useArticleStore()
        // console.log(to)
        // console.log(from)
        if (!store.isLogin) {
          return {name: 'home'}
        }
      }
    },
    
  ]
})

export default router
