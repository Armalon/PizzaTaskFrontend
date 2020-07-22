<template>
    <div id="app">
        <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
            <logo></logo>
        </div>

        <router-view></router-view>
    </div>
</template>

<script>
    import Logo from './components/Logo.vue'

    export default {
        name: 'App',
        components: {
            Logo
        }
    }
</script>

<style>
</style>
