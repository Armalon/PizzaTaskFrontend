<template>
    <div>
        <div class="px-3 py-3 pb-md-4 mx-auto text-center">
            <h1 class="display-4">Menu</h1>
            <p class="lead">
                Our delicious pizza will not leave you indifferent
            </p>
        </div>

        <div class="container">
            <search-filters></search-filters>

            <div class="card-deck mb-3 text-center">
                <menu-element></menu-element>
                <menu-element></menu-element>
                <menu-element></menu-element>
            </div>
        </div>

    </div>
</template>

<script>
    import SearchFilters from "./SearchFilters";
    import MenuElement from "./MenuElement";

    export default {
        data() {
            return {
                chatList: null
            }
        },
        methods: {
            authorizeMe() {
                this.axios.get('http://localhost:5000/login', { withCredentials: true }).then((response) => {
                    if (response.data
                        && !response.data.error
                        && response.data.user) {

                        this.$store.dispatch('setIAmAuthorized', response.data.user);
                    }
                })
            },
            loggingMeOut() {
                this.axios.get('http://localhost:5000/logout', { withCredentials: true }).then((response) => {
                    if (response.data
                        && !response.data.error) {

                        this.$store.dispatch('setIAmAuthorized', null);
                    }
                })
            },
        },
        created() {
            setInterval(() => {
                if (this.iAmAuthorized) {
                    // this.axios.get('http://localhost:5000/mychats', { withCredentials: true }).then((response) => {
                    //     if (response.data
                    //         && !response.data.error
                    //         && response.data.chats) {
                    //
                    //         this.chatList = response.data.chats;
                    //     }
                    // })
                }
            }, 1000);
        },
        components: {
            SearchFilters,
            MenuElement
        },
    }
</script>