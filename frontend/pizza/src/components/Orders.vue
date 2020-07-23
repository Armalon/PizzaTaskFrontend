<template>
    <div>
        <div class="px-3 py-3 pb-md-4 mx-auto text-center">
            <h1 class="display-4">Your Orders</h1>
            <p class="lead">
            </p>
        </div>

        <div class="container">
            <span class="h3" v-if="!iAmAuthorized">
                You need to be authorized to see your orders list.
            </span>

            <div v-if="iAmAuthorized">
                <div class="text-center" v-if="ordersList == null">
                    <div class="spinner-border text-warning" style="width: 3rem; height: 3rem;" role="status">
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>

                <table class="table" v-if="ordersList">
                    <thead>
                    <tr class="">
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col">Address</th>
                        <th scope="col">Phone</th>
                        <th scope="col">Created</th>
                        <th scope="col">Status</th>
                        <th scope="col">Total price</th>
                    </tr>
                    </thead>
                    <tbody>
                        <order-row v-for="element in ordersList" :element="element" :key="element.id"></order-row>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import OrderRow from "./OrderRow";

    export default {
        data() {
            return {
                ordersList: null
            }
        },
        methods: {
            initOrdersList() {
                this.axios.get('http://localhost:5000/my_orders',{ withCredentials: true }).then((response) => {
                    console.log('response', response);

                    if (response.data
                        && !response.data.error
                        && response.data.orders_list) {

                        this.ordersList = response.data.orders_list
                    }
                })
            }
        },
        watch: {
            iAmAuthorized() {
                this.initOrdersList()
            }
        },
        created() {
            this.initOrdersList()
        },
        components: {
            OrderRow
        }
    }
</script>