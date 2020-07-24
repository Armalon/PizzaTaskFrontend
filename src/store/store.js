import Vue from 'vue';
import Vuex from 'vuex';

import VuexPersistence from 'vuex-persist'

Vue.use(Vuex);

const vuexPersist = new VuexPersistence({
    key: 'firstchat',
    storage: localStorage
});

const state = {
    iAmAuthorized: null, // null or user data
    cart: [], // { id: 123, quantity: 2 }
    serviceInfo: null,
    currency: 'usd',
}

const mutations = {
    'SET_I_AM_AUTHORIZED' (state, user) {
        state.iAmAuthorized = user;
    },
    'SET_TO_CART' (state, { id, element, quantity }) {
        let foundElIndex = state.cart.findIndex(el => el.id === id)
        if (foundElIndex === -1) {
            if (quantity) {
                state.cart.push({id, element, quantity})
            }
        } else {
            state.cart[foundElIndex].quantity += quantity

            if (!state.cart[foundElIndex].quantity) {
                state.cart.splice(foundElIndex, 1)
            }
        }
    },
    'SET_SERVICE_INFO' (state, info) {
        state.serviceInfo = info
    },
    'SET_CURRENCY' (state, currency) {
        state.currency = currency
    },
    'CLEAR_CART' (state) {
        state.cart = []
    }
}

const actions = {
    setIAmAuthorized: ({ commit }, user) => {
        commit('SET_I_AM_AUTHORIZED', user);
    },
    // quantity can be negative
    setToCart: ({ commit }, { id, element, quantity }) => {
        if (typeof quantity === 'undefined') {
            quantity = 1
        }
        commit('SET_TO_CART', { id, element, quantity })
    },
    removeFromCart: ({ commit, state }, { id }) => {
        let foundElIndex = state.cart.findIndex(el => el.id === id)
        if (foundElIndex !== -1) {
            commit('SET_TO_CART', { id, quantity: - state.cart[foundElIndex].quantity })
        }
    },
    clearCart: ({ commit }) => {
        commit('CLEAR_CART')
    },
    setServiceInfo: ({ commit }, info)  => {
        commit('SET_SERVICE_INFO', info)
    },
    setCurrency: ({ commit }, currency) => {
        commit('SET_CURRENCY', currency)
    },
}

const getters = {
    iAmAuthorized: state => {
        return state.iAmAuthorized;
    },
    getCart: state => {
        return state.cart
    },
    isInTheCart: (state) => (id) => {
        let foundElIndex = state.cart.findIndex(el => el.id === id)
        return foundElIndex !== -1 && state.cart[foundElIndex].quantity
    },
    deliveryPrice: (state) => {
        return state.serviceInfo ? state.serviceInfo.delivery_price : null
    },
    usdToEurMultiplier: (state) => {
        return state.serviceInfo ? state.serviceInfo.usd_to_eur_multiplier : 1
    },
    currency: state => state.currency,
}

export const store = new Vuex.Store({
    state,
    mutations,
    actions,
    getters,
    plugins: [vuexPersist.plugin]
});