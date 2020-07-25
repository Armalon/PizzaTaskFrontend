<template>
    <div class="my-1 px-3 py-1">
        <button
                v-if="!iAmAuthorized"
                class="btn btn-outline-primary my-2"
                @click="logIn"
                title="You will get random user credential">Sign in</button>

        <button
                v-if="iAmAuthorized"
                class="btn btn-outline-primary my-2"
                @click="loggingMeOut"
                :disabled="requestIsInProcess"
                title="">Sign out</button>

        <div v-if="!iAmAuthorized && !requestIsInProcess" class="alert alert-primary" role="alert">
            You will get random user credential
        </div>

        <div v-if="iAmAuthorized && !requestIsInProcess" class="alert alert-success" role="alert">
            Hello, <b><i>{{ userName }}</i></b>
        </div>

        <loader v-if="requestIsInProcess"></loader>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                requestIsInProcess: false
            }
        },
        methods: {
            logIn() {
                this.requestIsInProcess = true;

                this.authorizeMe()
                    .finally(() => {
                        this.requestIsInProcess = false;
                    });
            },
            loggingMeOut() {
                this.requestIsInProcess = true;

                this.axios.get('/logout', { withCredentials: true }).then((response) => {
                        if (response.data
                            && !response.data.error) {

                            this.$store.dispatch('setIAmAuthorized', null);
                        }
                    })
                    .finally(() => {
                        this.requestIsInProcess = false;
                    });
            },
        },
    }
</script>
