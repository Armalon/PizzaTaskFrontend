<template>
    <div class="page-content page-container" id="page-content">
        <div class="padding">
            <div class="row container d-flex justify-content-center">
                <div class="col-md-6">
                    <div class="card card-bordered">
                        <div class="card-header">
                            <h4 class="card-title"><strong>Chat</strong></h4>
<!--                            <a class="btn btn-xs btn-secondary" href="#" data-abc="true">Let's Chat App</a>-->
                        </div>
                        <div class="ps-container ps-theme-default ps-active-y" id="chat-content" style="overflow-y: scroll !important; height:400px !important;">
                            <ChatMessage v-for="chat in chatMessages" :key="chat.id" :chat="chat" />

                            <!--
                            <div class="media media-chat"> <img class="avatar" src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="...">
                                <div class="media-body">
                                    <p>Hi</p>
                                    <p>How are you ...???</p>
                                    <p>What are you doing tomorrow?<br> Can we come up a bar?</p>
                                    <p class="meta"><time datetime="2018">23:58</time></p>
                                </div>
                            </div>

                            <div class="media media-chat"> <img class="avatar" src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="...">
                                <div class="media-body">
                                    <p>Okay</p>
                                    <p>We will go on sunday? </p>
                                    <p class="meta"><time datetime="2018">00:07</time></p>
                                </div>
                            </div>
                            <div class="media media-chat media-chat-reverse">
                                <div class="media-body">
                                    <p>That's awesome!</p>
                                    <p>I will meet you Sandon Square sharp at 10 AM</p>
                                    <p>Is that okay?</p>
                                    <p class="meta"><time datetime="2018">00:09</time></p>
                                </div>
                            </div>
                            <div class="media media-chat"> <img class="avatar" src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="...">
                                <div class="media-body">
                                    <p>Okay i will meet you on Sandon Square </p>
                                    <p class="meta"><time datetime="2018">00:10</time></p>
                                </div>
                            </div>
                            <div class="media media-chat media-chat-reverse">
                                <div class="media-body">
                                    <p>Do you have pictures of Matley Marriage?</p>
                                    <p class="meta"><time datetime="2018">00:10</time></p>
                                </div>
                            </div>
                            <div class="media media-chat"> <img class="avatar" src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="...">
                                <div class="media-body">
                                    <p>Sorry I don't have. i changed my phone.</p>
                                    <p class="meta"><time datetime="2018">00:12</time></p>
                                </div>
                            </div>
                            <div class="media media-chat media-chat-reverse">
                                <div class="media-body">
                                    <p>Okay then see you on sunday!!</p>
                                    <p class="meta"><time datetime="2018">00:12</time></p>
                                </div>
                            </div>
                            -->
                            <div class="ps-scrollbar-x-rail" style="left: 0px; bottom: 0px;">
                                <div class="ps-scrollbar-x" tabindex="0" style="left: 0px; width: 0px;"></div>
                            </div>
                            <div class="ps-scrollbar-y-rail" style="top: 0px; height: 0px; right: 2px;">
                                <div class="ps-scrollbar-y" tabindex="0" style="top: 0px; height: 2px;"></div>
                            </div>

                        </div>
                        <div class="publisher bt-1 border-light">
                            <img class="avatar avatar-xs"
                                 src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="...">

                            <input
                                    v-model="currentMessageText"
                                    class="publisher-input"
                                    type="text"
                                    placeholder="Write something"
                                    @keydown.enter.exact.prevent="sendMessage">

                            <span class="publisher-btn file-group">
                                <i class="fa fa-paperclip file-browser"></i>
                                <input type="file">
                            </span>
                            <a class="publisher-btn" href="#" data-abc="true">
                                <i class="fa fa-smile"></i>
                            </a>
                            <a class="publisher-btn text-info" href="#" data-abc="true">
                                <i class="fa fa-paper-plane"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ChatMessage from "./ChatMessage";

    export default {
        name: 'LiveChat',
        props: ['chatId'],
        data() {
            return {
                checkInterval: null,
                chatMessages: null,
                currentMessageText: '',
            }
        },
        methods: {
            sendMessage() {
                if (!this.currentMessageText.trim()) {
                    return;
                }
                const messageText = this.currentMessageText;
                this.currentMessageText = '';

                this.sendPost({ messageText });
            },
            sendPost({ messageText }) {
                this.axios.get('http://localhost:5000/chat-post-message',
                    { params: { chat_id: this.chatId, text: messageText }, withCredentials: true }
                ).then((response) => {
                    if (response.data
                        && !response.data.error
                        && response.data.message) {

                        // do nothing
                    }
                })
            }
        },
        created() {
            let that = this;
            this.checkInterval = setInterval(function () {
                that.axios.get('http://localhost:5000/chat-messages',
                    { params: { chat_id: that.chatId }, withCredentials: true }
                ).then((response) => {
                    if (response.data
                        && !response.data.error
                        && response.data.messages) {

                        that.chatMessages = response.data.messages;
                    }
                })
            }, 1000);
        },
        beforeDestroy() {
            if (typeof this.checkInterval !== 'undefined') {
                clearInterval(this.checkInterval);
                this.checkInterval = null;
            }
        },
        components: {
            ChatMessage
        },
    }
</script>

<style></style>