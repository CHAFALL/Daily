import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// PageTitle이 많은 곳에 쓰일 것 같아서 전역으로...
import PageTitle from './components/fragments/PageTitle.vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret, faUserClock } from '@fortawesome/free-solid-svg-icons'

import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

import { LoadingPlugin } from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css'

/* add icons to the library */
library.add(faUserSecret)
library.add(faUserClock)

// createApp(App).use(store).use(router).mount('#app')
const app = createApp(App)
app.use(store)
app.use(router)
app.use(VueSweetalert2)
app.use(LoadingPlugin)
app.component('page-title', PageTitle)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
