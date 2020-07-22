import Vue from 'vue';
import Vuex from 'vuex';

import VuexPersistence from 'vuex-persist'

Vue.use(Vuex);

const vuexPersist = new VuexPersistence({
    key: 'firstchat',
    storage: localStorage
});

const state = {
    iAmAuthorized: null // null or user data
}

const mutations = {
    'SET_I_AM_AUTHORIZED' (state, user) {
        state.iAmAuthorized = user;
    },
}

const actions = {
    setIAmAuthorized: ({ commit }, user) => {
        commit('SET_I_AM_AUTHORIZED', user);
    },
}

const getters = {
    iAmAuthorized: state => {
        return state.iAmAuthorized;
    },
}

export const store = new Vuex.Store({
    state,
    mutations,
    actions,
    getters,
    plugins: [vuexPersist.plugin]
});