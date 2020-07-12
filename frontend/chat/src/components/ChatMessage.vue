<template>
    <div>
<!--        <div class="media media-meta-day">Today</div>-->
<!--        media-chat-reverse CLASS -->
        <div class="media media-chat" :class="{ 'media-chat-reverse': iAmAuthorized && chat.user_id == iAmAuthorized.id }">
            <div class="media-body">
                <p>{{ chat.text }}</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['chat'],
        data() {
            return {
            }
        }
    }
</script>

<style></style>