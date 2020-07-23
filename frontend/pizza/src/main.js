import Vue from 'vue'
import App from './App.vue'

import { store } from './store/store.js';

import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router'

import Home from "./components/Home";
import Contacts from "./components/Contacts";

Vue.config.productionTip = false

Vue.mixin({
    computed: {
        iAmAuthorized() {
            return this.$store.getters.iAmAuthorized;
        },
        username() {
            return this.iAmAuthorized && this.iAmAuthorized.name ? this.iAmAuthorized.name : null
        }
    },
    filters: {
        capitalize: function (value) {
            if (!value) return ''
            value = value.toString().toLowerCase()
            return value.charAt(0).toUpperCase() + value.slice(1)
        }
    }
})

Vue.use(VueAxios, axios)

Vue.use(VueRouter)

const routes = [
    {
        name: 'home',
        path: '/',
        component: Home,
    },
    {
        name: 'contacts',
        path: '/contacts',
        component: Contacts,
    },
];

const router = new VueRouter(
    {
        mode: 'history',
        routes,
    }
);

new Vue({
    store,
    router,
    render: h => h(App),
}).$mount('#app')
