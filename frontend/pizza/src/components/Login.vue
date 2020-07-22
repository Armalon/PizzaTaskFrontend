<template>
    <div class="my-2">
        <div v-if="!iAmAuthorized">
            <p>
                You need to be authorized to get access to the chat. You will get random user credential by pressing a button below.
            </p>
            <button class="btn btn-outline-primary" @click="authorizeMe">Authorise me</button>
        </div>

        <div v-if="iAmAuthorized">
            <p>
                Now you are authorized. Hello <b><i>{{ username }}</i></b>
            </p>

            <button class="btn btn-outline-primary" @click="loggingMeOut">Logging out</button>
        </div>
    </div>
</template>

<script>
    export default {
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
    }
</script>
