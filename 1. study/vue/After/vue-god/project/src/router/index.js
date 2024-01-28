import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/databinding/string',
    name: 'DataBindingStringView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingStringView.vue'
      )
  },
  {
    path: '/databinding/html',
    name: 'DataBindingHtmlView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingHtmlView.vue'
      )
  },
  {
    path: '/databinding/input',
    name: 'DataBindingInputView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingInputView.vue'
      )
  },
  {
    path: '/databinding/select',
    name: 'DataBindingSelectView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingSelectView.vue'
      )
  },
  {
    path: '/databinding/check',
    name: 'DataBindingCheckboxView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingCheckboxView.vue'
      )
  },
  {
    path: '/databinding/radio',
    name: 'DataBindingRadioView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingRadioView.vue'
      )
  },
  {
    path: '/databinding/attr',
    name: 'DataBindingAttributeView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingAttributeView.vue'
      )
  },
  {
    path: '/databinding/list',
    name: 'DataBindingListView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingListView.vue'
      )
  },
  {
    path: '/databinding/class',
    name: 'DataBindingClassView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingClassView.vue'
      )
  },
  {
    path: '/databinding/style',
    name: 'DataBindingStyleView',
    component: () =>
      import(
        /* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingStyleView.vue'
      )
  },
  {
    path: '/event/click',
    name: 'EventClickView',
    component: () =>
      import(
        /* webpackChunkName: "event", webpackPrefetch:true */ '../views/2_event/EventClickView.vue'
      )
  },
  {
    path: '/event/change',
    name: 'EventChangeView',
    component: () =>
      import(
        /* webpackChunkName: "event", webpackPrefetch:true */ '../views/2_event/EventChangeView.vue'
      )
  },
  {
    path: '/event/key',
    name: 'EventKeyView',
    component: () =>
      import(
        /* webpackChunkName: "event", webpackPrefetch:true */ '../views/2_event/EventKeyView.vue'
      )
  },
  {
    path: '/extra/if',
    name: 'RenderingIfView',
    component: () =>
      import(
        /* webpackChunkName: "extra", webpackPrefetch:true */ '../views/3_extra/RenderingIfView.vue'
      )
  },
  {
    path: '/extra/show',
    name: 'RenderingShowView',
    component: () =>
      import(
        /* webpackChunkName: "extra", webpackPrefetch:true */ '../views/3_extra/RenderingShowView.vue'
      )
  },
  {
    path: '/extra/computed',
    name: 'ComputedView',
    component: () =>
      import(
        /* webpackChunkName: "extra", webpackPrefetch:true */ '../views/3_extra/ComputedView.vue'
      )
  },
  {
    path: '/extra/watch',
    name: 'WatchView',
    component: () =>
      import(
        /* webpackChunkName: "extra", webpackPrefetch:true */ '../views/3_extra/WatchView.vue'
      )
  },
  {
    path: '/extra/lifecycle',
    name: 'LifecycleHookView',
    component: () =>
      import(
        /* webpackChunkName: "extra", webpackPrefetch:true */ '../views/3_extra/LifecycleHookView.vue'
      )
  },
  {
    path: '/reuse/pagetitle',
    name: 'PageView',
    component: () =>
      import(
        /* webpackChunkName: "reuse", webpackPrefetch:true */ '../views/4_reuse/PageView.vue'
      )
  },
  {
    path: '/reuse/parent',
    name: 'ParentView',
    component: () =>
      import(
        /* webpackChunkName: "reuse", webpackPrefetch:true */ '../views/4_reuse/ParentView.vue'
      )
  },
  {
    path: '/reuse/list',
    name: 'ListView',
    component: () =>
      import(
        /* webpackChunkName: "reuse", webpackPrefetch:true */ '../views/4_reuse/ListView.vue'
      )
  },
  {
    path: '/reuse/slot',
    name: 'SlotView',
    component: () =>
      import(
        /* webpackChunkName: "reuse", webpackPrefetch:true */ '../views/4_reuse/SlotView.vue'
      )
  },
  {
    path: '/advanced/provide',
    name: 'ProvideView',
    component: () =>
      import(
        /* webpackChunkName: "advanced", webpackPrefetch:true */ '../views/5_advanced/ProvideView.vue'
      )
  }
]

// webpackPrefetch:true의 기능: 캐시 미리 받아둠.(용량이 큰데 미래에도 많이 이용이 될 것이면 Good)(잘 안 쓴다면 쓸때없이 받아두는 거라 Bad)
// 즉 자주 쓰이는 곳이면 받아두는 것을 권장. (이 부분 꽤 중요!!)

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
