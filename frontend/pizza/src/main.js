import Vue from 'vue'
import App from './App.vue'

import { store } from './store/store.js';

import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router'
import moment from 'moment';

import Home from "./components/Home";
import Contacts from "./components/Contacts";
import MakeOrder from "./components/MakeOrder";
import Orders from "./components/Orders";

Vue.config.productionTip = false

Vue.mixin({
    methods: {
        addToCart(element) {
            this.setToCart(element.id, element, 1)
        },
        removeFromCart(element) {
            this.$store.dispatch('removeFromCart', { id: element.id })
        },
        setToCart(id, element, quantity) {
            this.$store.dispatch('setToCart', { id, element, quantity })
        },
        authorizeMe(event, userId) {
            this.axios.post('http://localhost:5000/login', { user_id: userId }, { withCredentials: true }).then((response) => {
                if (response.data
                    && !response.data.error
                    && response.data.user) {

                    this.$store.dispatch('setIAmAuthorized', response.data.user);
                }
            })
        },
        formatPriceByCurrency(amount) {
            if (this.globalCurrency == 'usd') {
                return '$' + amount;
            } else {
                return this.roundToTwo(amount * this.usdToEurMultiplier) + '€';
            }
        },
        roundToTwo(num) {
            return +(Math.round(num + "e+2")  + "e-2");
        },
    },
    computed: {
        iAmAuthorized() {
            return this.$store.getters.iAmAuthorized;
        },
        userName() {
            return this.iAmAuthorized && this.iAmAuthorized.name ? this.iAmAuthorized.name : null
        },
        userPhone() {
            return this.iAmAuthorized && this.iAmAuthorized.phone ? this.iAmAuthorized.phone : null
        },
        userAddress() {
            return this.iAmAuthorized && this.iAmAuthorized.address ? this.iAmAuthorized.address : null
        },
        cartGlobal() {
            return this.$store.getters.getCart;
        },
        totalCartItems() {
            let totalItems = 0
            for (let i in this.cartGlobal) {
                totalItems += this.cartGlobal[i].quantity
            }
            return totalItems
        },
        totalCartPrice() {
            let totalPrice = 0
            for (let i in this.cartGlobal) {
                totalPrice += this.cartGlobal[i].quantity * this.cartGlobal[i].element.price
            }
            return totalPrice
        },
        deliveryPrice() {
            return this.$store.getters.deliveryPrice;
        },
        usdToEurMultiplier() {
            return this.$store.getters.usdToEurMultiplier;
        },
        globalCurrency() {
            return this.$store.getters.currency;
        },
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
    /*
    {
        name: 'contacts',
        path: '/contacts',
        component: Contacts,
    },
     */
    {
        name: 'cart',
        path: '/cart',
        component: MakeOrder,
    },
    {
        name: 'orders',
        path: '/orders',
        component: Orders,
    },
];

const router = new VueRouter(
    {
        mode: 'history',
        routes,
    }
);

function MomentumFormat(formatString, value) {
    if (value) {
        const momentTime = moment(value * 1000);
        return momentTime.format(formatString);
    }
}

Vue.filter('formatTimestampDateTime', function(value, currentTimezone) {
    // September 4 1986 8:30 PM
    return MomentumFormat('LLL', value, currentTimezone);
});

new Vue({
    store,
    router,
    render: h => h(App),
}).$mount('#app')
