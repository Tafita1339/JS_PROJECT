import Vue from 'vue'
import app from './App.vue'

import axios from 'axios'

import VueAxios from 'vue-axios'

import "bootstrap/dist/css/bootstrap.min.css"
import 'bootstrap/dist/js/bootstrap.min.js'

import router from './router';

Vue.use(VueAxios, axios)

Vue.config.productionTip =  true

new Vue({
  router,
  render: h => h(app)
}).$mount('#app')