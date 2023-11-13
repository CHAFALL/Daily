import PiniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { PiniaVuePlugin, createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

pinia.use(PiniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)

app.mount('#app')
