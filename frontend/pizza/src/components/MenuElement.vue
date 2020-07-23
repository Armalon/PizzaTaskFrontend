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
                <li class="list-group-item">Size: {{ element.size | capitalize }}</li>
                <li class="list-group-item">Weight: {{ element.weight }} gram</li>
            </ul>
        </div>
        <div class="card-footer">
            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <button class="btn btn-success">-</button>
                </div>
                <input class="form-control" type="number" readonly>
                <div class="input-group-append">
                    <button class="btn btn-success">+</button>
                </div>
            </div>

            <button type="button" class="btn btn-lg btn-block btn-success" @click="addToCart(element)">
                Add to cart
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
        }
    }
</script>