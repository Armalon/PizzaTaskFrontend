import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
    iAmAuthorized: false
}

const mutations = {
}

const actions = {
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
    getters
});