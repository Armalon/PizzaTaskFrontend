<template>
    <div>
        <div class="px-3 py-3 pb-md-4 mx-auto text-center">
            <h1 class="display-4">Your Cart</h1>
            <p class="lead">
            </p>
        </div>

        <div class="container">
            <table class="table" v-if="totalCartItems">
                <thead>
                    <tr class="">
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col" class="pl-4">Quantity</th>
                        <th scope="col">Remove</th>
                        <th scope="col">Price</th>
                    </tr>
                </thead>
                <tbody>
                    <cart-row
                            v-for="cartElement in cartGlobal"
                            :element="cartElement.element"
                            :cartElement="cartElement"
                            :key="cartElement.element.id"></cart-row>
                </tbody>
            </table>
            <span class="h3" v-if="!totalCartItems">
                There is no products in your cart, please <router-link :to="{name: 'home'}">check our Menu</router-link>
            </span>
        </div>
    </div>
</template>


<script>
    import CartRow from "./CartRow";

    export default {
        components: {
            CartRow
        }
    }
</script>