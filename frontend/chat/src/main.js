import Vue from 'vue'
import App from './App.vue'

import { store } from './store/store.js';

import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router'
import LiveChat from "./components/LiveChat";

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
})

Vue.use(VueAxios, axios)

Vue.use(VueRouter)

const routes = [
    {
        name: 'home',
        path: '/',
        component: App,
    },
    {
        name: 'chat',
        path: '/chat/:chatId',
        component: LiveChat,
        props: true,
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
