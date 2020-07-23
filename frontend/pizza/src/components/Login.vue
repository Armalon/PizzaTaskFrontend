<template>
    <div class="my-2 p-4">
        <div v-if="!iAmAuthorized">
            <button
                    class="btn btn-outline-primary my-2"
                    @click="authorizeMe"
                    title="You will get random user credential">Sign in</button>

            <div class="alert alert-primary" role="alert">
                You will get random user credential
            </div>
        </div>

        <div v-if="iAmAuthorized">
            <button
                    class="btn btn-outline-primary my-2"
                    @click="loggingMeOut"
                    title="">Sign out</button>

            <div class="alert alert-success" role="alert">
                Hello, <b><i>{{ userName }}</i></b>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        methods: {
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
