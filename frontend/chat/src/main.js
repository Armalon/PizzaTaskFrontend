import Vue from 'vue'
import App from './App.vue'

import { store } from './store/store.js';

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

Vue.mixin({
    computed: {
        iAmAuthorized() {
            return this.$store.getters.iAmAuthorized;
        }
    },
})

Vue.use(VueAxios, axios)

new Vue({
    store,
    render: h => h(App),
}).$mount('#app')
