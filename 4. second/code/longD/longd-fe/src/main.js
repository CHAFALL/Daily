import './style.css';
import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

const app = createApp(App);

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core';

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

/* import specific icons */
import { faUserSecret, faPhone } from '@fortawesome/free-solid-svg-icons';
import { faImage, faCalendarCheck } from '@fortawesome/free-regular-svg-icons';

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

/* add icons to the library */
library.add(faUserSecret, faImage, faCalendarCheck, faPhone);

app.use(createPinia());
app.use(router);
app.use(VueSweetalert2);
app.component('font-awesome-icon', FontAwesomeIcon);
app.mount('#app');
