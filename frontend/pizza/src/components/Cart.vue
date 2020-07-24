<template>
    <div class="text-right my-2 ml-md-auto">
        <div class="card">
            <div class="card-body">
                <div class="h3 card-title">
                    <svg width="1em" height="1.2em" viewBox="0 0 16 16" class="bi bi-cart4" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l.5 2H5V5H3.14zM6 5v2h2V5H6zm3 0v2h2V5H9zm3 0v2h1.36l.5-2H12zm1.11 3H12v2h.61l.5-2zM11 8H9v2h2V8zM8 8H6v2h2V8zM5 8H3.89l.5 2H5V8zm0 5a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
                    </svg>
                    Cart
                </div>
                <router-link :to="{ name: 'cart' }" v-if="totalCartItems">
                    <ul class="list-unstyled card-text">
                        <li class="text-nowrap">Items ... {{ totalCartItems }}</li>
                        <li class="text-nowrap">Total price ... {{ formatPriceByCurrency(totalCartPrice) }}</li>
                    </ul>
                </router-link>
                <div v-if="!totalCartItems">
                    Nothing here yet
                </div>

                <currencies></currencies>
            </div>
        </div>
    </div>
</template>

<script>
    import Currencies from "./Currencies";

    export default {
        computed: {
        },
        components: {
            Currencies
        }
    }
</script>