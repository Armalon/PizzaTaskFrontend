<template>
    <div id="app">
        <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
            <logo></logo>

            <navigation></navigation>

            <login></login>

            <cart></cart>
        </div>

        <router-view></router-view>
    </div>
</template>

<script>
    import Logo from './components/Logo.vue'
    import Navigation from "./components/Navigation"
    import Cart from "./components/Cart";
    import Login from "./components/Login";

    export default {
        name: 'App',
        components: {
            Logo,
            Navigation,
            Cart,
            Login
        },
        methods: {
            getServiceInfo() {
                this.axios.get('http://localhost:5000/service_info', { withCredentials: true }).then((response) => {
                    if (response.data
                        && !response.data.error
                        && response.data.info) {

                        this.$store.dispatch('setServiceInfo', response.data.info);
                    }
                })
            },
        },
        created() {
            this.getServiceInfo()
        }
    }
</script>

<style>
</style>
