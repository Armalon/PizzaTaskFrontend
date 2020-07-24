<template>
    <nav class="navbar navbar-light bg-light navbar-brand px-2 py-4 my-2 my-md-0 mr-md-3">
        <router-link class="p-2 text-dark" :to="{ name: 'home' }">Menu</router-link>
        <router-link v-if="iAmAuthorized" class="p-2 text-dark text-nowrap" :to="{ name: 'orders' }">My orders</router-link>
        <router-link class="p-2 text-dark" :to="{ name: 'contacts' }">Contacts</router-link>
    </nav>
</template>

<script>
    export default {

    }
</script>

<style>
    .router-link-exact-active {
        font-weight: bold;
    }
</style>