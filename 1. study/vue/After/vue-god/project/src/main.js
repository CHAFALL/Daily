import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// PageTitle이 많은 곳에 쓰일 것 같아서 전역으로...
import PageTitle from './components/fragments/PageTitle.vue'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

// createApp(App).use(store).use(router).mount('#app')
const app = createApp(App)
app.use(store)
app.use(router)
app.component('page-title', PageTitle)
app.mount('#app')
