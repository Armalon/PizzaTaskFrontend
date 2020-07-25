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

            <span class="h4" v-if="ordersList && ordersList.length == 0">
                You have no orders yet, please <router-link :to="{name: 'home'}">check our Menu</router-link> to make one
            </span>

            <div v-if="iAmAuthorized">
                <div class="text-center" v-if="ordersList == null">
                    <div class="spinner-border text-warning" style="width: 3rem; height: 3rem;" role="status">
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>

                <table class="table" v-if="ordersList && ordersList.length > 0">
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
    import OrderRow from "../OrderRow";

    export default {
        data() {
            return {
                ordersList: null,
                checkInterval: null
            }
        },
        methods: {
            initOrdersList() {
                if (this.iAmAuthorized) {
                    this.axios.get('/my_orders',{ withCredentials: true }).then((response) => {
                        if (response.data
                            && !response.data.error
                            && response.data.orders_list) {

                            this.ordersList = response.data.orders_list
                        }
                    })
                } else {
                    this.ordersList = null
                }
            }
        },
        watch: {
            iAmAuthorized() {
                this.initOrdersList()
            }
        },
        created() {
            this.checkInterval = setInterval(() => {
                this.initOrdersList()
            }, 1000)
        },
        beforeDestroy() {
            if (typeof this.checkInterval !== 'undefined') {
                clearInterval(this.checkInterval);
                this.checkInterval = null;
            }
        },
        components: {
            OrderRow
        }
    }
</script>