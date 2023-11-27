// Plugins
import { registerPlugins } from '@/plugins'

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

// // 옆으로 넘기는 기능
// import { Swiper as SwiperClass, Pagination, Navigation } from 'swiper/core';
// import getAwesomeSwiper from 'vue-awesome-swiper/dist/exporter';
// import 'swiper/swiper-bundle.css';
// app.component('swiper', Swiper);
// app.component('swiper-slide', SwiperSlide);
// SwiperClass.use([Pagination, Navigation]);
// const { Swiper, SwiperSlide } = getAwesomeSwiper();

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.use(router)

registerPlugins(app)

app.mount('#app')
