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
    cart: [] // { id: 123, quantity: 2 }
}

const mutations = {
    'SET_I_AM_AUTHORIZED' (state, user) {
        state.iAmAuthorized = user;
    },
    'SET_TO_CART' (state, { id, quantity }) {
        let foundElIndex = state.cart.findIndex(el => el.id === id)
        if (foundElIndex === -1) {
            state.cart.push({ id, quantity })
        } else {
            state.cart[foundElIndex].quantity += quantity
        }
    }
}

const actions = {
    setIAmAuthorized: ({ commit }, user) => {
        commit('SET_I_AM_AUTHORIZED', user);
    },
    // quantity can be negative
    setToCart: ({ commit }, { id, quantity }) => {
        if (typeof quantity === 'undefined') {
            quantity = 1
        }
        commit('SET_TO_CART', { id, quantity })
    },
    removeFromCart: ({ commit, state }, { id }) => {
        if (state.cart[id]) {
            commit('SET_TO_CART', { id, quantity: state.cart[id].quantity })
        }
    },
}

const getters = {
    iAmAuthorized: state => {
        return state.iAmAuthorized;
    },
    getCart: state => {
        return state.cart
    },
}

export const store = new Vuex.Store({
    state,
    mutations,
    actions,
    getters,
    plugins: [vuexPersist.plugin]
});