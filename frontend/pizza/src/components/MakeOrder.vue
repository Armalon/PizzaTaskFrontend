<template>
    <div>
        <div class="px-3 py-3 pb-md-4 mx-auto text-center">
            <h1 class="display-4">Your Cart</h1>
            <p class="lead">
            </p>
        </div>

        <div class="container">
            <span class="h3" v-if="orderPlaced">
                Thank you! Your order has been placed, please wait for our manager to contact you for confirmation.
                <br>
                You can check it's status in a <router-link :to="{ name: 'orders'}">orders list</router-link>
            </span>

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

                    <tr v-if="deliveryPrice">
                        <th>Delivery price</th>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td>{{ formatPriceByCurrency(deliveryPrice) }}</td>
                    </tr>

                    <tr>
                        <th>Total price</th>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td>{{ formatPriceByCurrency(totalCartPrice + (deliveryPrice ? deliveryPrice : 0)) }}</td>
                    </tr>
                </tbody>
            </table>
            <span class="h3" v-if="!totalCartItems && !orderPlaced">
                There is no products in your cart, please <router-link :to="{name: 'home'}">check our Menu</router-link>
            </span>

            <div class="my-4 py-2" v-if="totalCartItems">
                <h2>Complete your order</h2>

                <form @submit.prevent="submitForm" autocomplete="off">
                    <div class="form-group">
                        <label for="name">Your Name</label>
                        <input v-model="name" type="text" class="form-control" id="name" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Your cellphone number</label>
                        <input v-model="phone" type="number" class="form-control" name="phone" id="phone" required :readonly="userPhone">
                        <small class="form-text text-muted">
                            Our operator will call you to confirm your order details.
                        </small>
                    </div>
                    <div class="form-group">
                        <label for="address">A delivery address</label>
                        <textarea v-model="address" class="form-control" id="address" required></textarea>
                    </div>

                    <button type="submit" class="btn btn-primary">Process order</button>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
    import CartRow from "./CartRow";

    export default {
        data() {
            return {
                name: '',
                phone: '',
                address: '',
                orderPlaced: false
            }
        },
        methods: {
            submitForm() {
                const formData = {
                    // getting rid of element field
                    order: this.cartGlobal.map(el => { let element; ({ element, ...el } = el); element; return el }),
                    // [
                    //     {
                    //         id, quantity
                    //     }
                    // ],
                    name: this.name,
                    phone: this.phone,
                    address: this.address,
                    // ...
                };

                this.axios.post('/make_order', formData,{ withCredentials: true }).then((response) => {
                    // console.log('response', response);

                    if (response.data
                        && !response.data.error) {

                        if (response.data.user) {
                            this.$store.dispatch('setIAmAuthorized', response.data.user);
                        }

                        if (response.data.order) {
                            this.orderPlaced = true
                            this.$store.dispatch('clearCart')
                        }
                    }
                })
            },
            refreshUserDataFromSession() {
                this.name = !this.name ? this.userName : this.name
                this.phone = this.userPhone
                this.address = !this.address ? this.userAddress : this.address
            }
        },
        created() {
            this.refreshUserDataFromSession()
        },
        watch: {
            userPhone() {
                this.refreshUserDataFromSession()
            }
        },
        components: {
            CartRow
        }
    }
</script>