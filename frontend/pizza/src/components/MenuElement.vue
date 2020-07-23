<template>
    <div class="card mb-4 shadow-sm">
        <img :src="'/img/pizza/' + element.picture + '.jpg'" class="card-img-top" alt="...">
        <div class="card-header">
            <h4 class="my-0 font-weight-normal">{{ element.name }}</h4>
        </div>
        <div class="card-body">
            <h2 class="card-title pricing-card-title">
                ${{ element.price }}
            </h2>
            <p class="card-text">
                {{ element.description }}
            </p>

            <ul class="list-group list-group-flush">
                <li class="list-group-item">Souse base: {{ element.base | capitalize}}</li>
                <li class="list-group-item">Pizza Crust: {{ element.crust | capitalize}}</li>
                <li class="list-group-item">Size: {{ element.size | capitalize }}</li>
                <li class="list-group-item">Weight: {{ element.weight }} gram</li>
            </ul>
        </div>
        <div class="card-footer">
             <div v-if="isInTheCart" class="input-group mb-3">
                <div class="input-group-prepend">
                    <button class="btn btn-success" @click="setToCart(element.id, element, -1)">-</button>
                </div>
                <input class="form-control text-center" type="number" readonly :value="isInTheCart">
                <div class="input-group-append">
                    <button class="btn btn-success" @click="addToCart(element)">+</button>
                </div>
            </div>

            <button v-if="!isInTheCart" type="button" class="btn btn-lg btn-block btn-success" @click="addToCart(element)">
                Add to cart
            </button>

            <button v-if="isInTheCart" type="button" class="btn btn-lg btn-block btn-warning" @click="removeFromCart(element)">
                Remove
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['element'],
        data() {
            return {

            }
        },
        methods: {
        },
        computed: {
            isInTheCart() {
                return this.$store.getters.isInTheCart(this.element.id)
            }
        }
    }
</script>