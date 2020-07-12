<template>
    <div>
        <div v-if="!iAmAuthorized">
            <p>
                You need to be authorized to get access to the chat. You will get random user credential by pressing a button below.
            </p>
            <button @click="authorizeMe">Authorise me</button>
        </div>

        <div v-if="iAmAuthorized">
            <p>
                Now you are authorized. Hello <b><i>{{ username }}</i></b>
            </p>

            <button @click="loggingMeOut">Logging out</button>
        </div>

        <div v-if="chatList">
            <br><br>
            <div v-for="chat in chatList" :key="chat.id">
                <router-link :to="{ name: 'chat', params: { chatId: chat.id } }">{{ chat.name }}</router-link>
                <br><br>
            </div>
        </div>
    </div>
</template>

<script>
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
                    this.axios.get('http://localhost:5000/mychats', { withCredentials: true }).then((response) => {
                        if (response.data
                            && !response.data.error
                            && response.data.chats) {

                            this.chatList = response.data.chats;
                        }
                    })
                }
            }, 1000);
        },
        components: {
        },
    }
</script>