import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from '@/router';
import globalDirectives from './plugins/global-directives';
import dayjs from './plugins/dayjs';
import { createPinia } from 'pinia';
// import focus from '@/directives/focus';
// import globalComponents from '@/plugins/global-components';

// createApp(App).use(router).mount('#app');

const app = createApp(App);
// app.use(globalComponents);
// app.directive('focus', focus);
app.use(router);
app.use(globalDirectives);
app.use(dayjs);
app.use(createPinia());
app.mount('#app');
import 'bootstrap/dist/js/bootstrap.js';

// console.log('MODE:', import.meta.env.MODE); // 개발모드인지 어떤 모드인지 출력해줌.
// console.log('MODE:', import.meta.env.BASE_URL); // 말 그대로 BASE_URL
// console.log('MODE:', import.meta.env.PROD); // 개발(production)모드면 true
// console.log('MODE:', import.meta.env.DEV); // DEV는 PROD의 반대
// console.log('VITE_APP_API_URL: ', import.meta.env.VITE_APP_API_URL);
