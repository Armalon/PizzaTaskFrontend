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
    import Logo from './components/base/Logo.vue'
    import Navigation from "./components/base/Navigation"
    import Cart from "./components/base/Cart";
    import Login from "./components/base/Login";

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
                this.axios.get('/service_info', { withCredentials: true }).then((response) => {
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
            if (this.iAmAuthorized) {
                this.authorizeMe(null, this.iAmAuthorized.id)
            }
        }
    }
</script>

<style>
</style>
