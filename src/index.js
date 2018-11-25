import Vue from 'vue';
import App from './App';
import axios from 'axios';

axios.defaults.baseURL = '/api/';
Vue.prototype.$api = axios;

new Vue({
  el: '#app',
  render: h => h(App),
});