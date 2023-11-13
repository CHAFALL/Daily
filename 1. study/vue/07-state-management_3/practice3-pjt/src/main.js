import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

// app.use(createPinia())
app.use(pinia)

app.mount('#app')



//`app.use(pinia)`를 사용하는 것은 이미 생성된 Pinia 인스턴스를 사용하는 것입니다. `createPinia()` 함수는 Pinia 인스턴스를 생성하고 반환합니다. 그리고 이 인스턴스에 `piniaPluginPersistedstate` 플러그인을 사용하도록 설정합니다.

//따라서 `const pinia = createPinia()`로 이미 Pinia 인스턴스를 생성했기 때문에, 해당 인스턴스를 재사용하여 애플리케이션에 Pinia를 추가하려면 `app.use(pinia)`를 사용합니다. 이렇게 하면 이미 구성된 Pinia 인스턴스가 애플리케이션에 추가되고, 이 인스턴스에는 이미 설정된 플러그인이 적용되어 있습니다.

//한편, `app.use(createPinia())`를 사용하는 경우에는 매번 애플리케이션에 대해 새로운 Pinia 인스턴스를 생성하게 됩니다. 이 경우에는 Pinia 인스턴스가 매번 새롭게 생성되므로 인스턴스 간의 상태 공유가 이루어지지 않습니다.

//따라서 이미 생성된 Pinia 인스턴스를 재사용하고자 할 때는 `app.use(pinia)`를 사용하는 것이 더 적절합니다.