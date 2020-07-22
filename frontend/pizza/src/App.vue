<template>
    <div id="app">
        <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
            <logo></logo>

            <navigation></navigation>

            <currencies></currencies>

            <cart></cart>
        </div>

        <router-view></router-view>
    </div>
</template>

<script>
    import Logo from './components/Logo.vue'
    import Navigation from "./components/Navigation"
    import Currencies from './components/Currencies'
    import Cart from "./components/Cart";

    export default {
        name: 'App',
        components: {
            Logo,
            Navigation,
            Currencies,
            Cart
        }
    }
</script>

<style>
</style>
