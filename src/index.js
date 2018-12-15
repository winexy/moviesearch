import Vue from 'vue';
import App from './App';
import axios from 'axios';

import router from './router';
import store from './store';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.baseURL = '/api/';

Vue.prototype.$api = axios;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');