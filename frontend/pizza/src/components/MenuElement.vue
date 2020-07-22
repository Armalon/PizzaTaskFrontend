<template>
    <div class="card mb-4 shadow-sm">
        <img src="../assets/portato_thin.jpg" class="card-img-top" alt="...">
        <div class="card-header">
            <h4 class="my-0 font-weight-normal">Portato</h4>
        </div>
        <div class="card-body">
            <h2 class="card-title pricing-card-title">
                $5
            </h2>
            <p class="card-text">
                sour cream sauce, mozzarella, boiled smoked shoulder, champignons, processed Cheddar cheese, garlic oil, herbs
            </p>

            <ul class="list-group list-group-flush">
                <li class="list-group-item">Weight: 1251 gramm</li>
                <li class="list-group-item">Size: Large</li>
            </ul>
        </div>
        <div class="card-footer">
            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <button class="btn btn-primary">-</button>
                </div>
                <input class="form-control" type="number">
                <div class="input-group-append">
                    <button class="btn btn-primary">+</button>
                </div>
            </div>


            <button type="button" class="btn btn-lg btn-block btn-primary">
                Add to cart
            </button>
        </div>
    </div>
</template>

<script>
    export default {
    }
</script>