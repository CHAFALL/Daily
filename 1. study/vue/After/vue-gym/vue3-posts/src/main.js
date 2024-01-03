import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from '@/router';
import funcPlugins from './plugins/func';
import objPlugins from './plugins/obj';
import person from './plugins/person';

// createApp(App).use(router).mount('#app');

const app = createApp(App);
app.use(funcPlugins);
app.use(objPlugins, { name: 'chafa' });
app.use(person, { name: '홍길동' });
app.use(router);
app.mount('#app');
import 'bootstrap/dist/js/bootstrap.js';

// console.log('MODE:', import.meta.env.MODE); // 개발모드인지 어떤 모드인지 출력해줌.
// console.log('MODE:', import.meta.env.BASE_URL); // 말 그대로 BASE_URL
// console.log('MODE:', import.meta.env.PROD); // 개발(production)모드면 true
// console.log('MODE:', import.meta.env.DEV); // DEV는 PROD의 반대
// console.log('VITE_APP_API_URL: ', import.meta.env.VITE_APP_API_URL);
