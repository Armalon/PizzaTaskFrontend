<template>
    <nav class="my-2 my-md-0 mr-md-3">
        <router-link class="p-2 text-dark" :to="{ name: 'home' }">Menu</router-link>
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