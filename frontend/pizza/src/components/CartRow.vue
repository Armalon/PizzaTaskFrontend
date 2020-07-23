<template>
    <tr>
        <th scope="row">1</th>
        <td>{{ element.name }}</td>
        <td>
            <div class="input-group mb-3 col-md-6 col-sm-12">
                <div class="input-group-prepend">
                    <button class="btn btn-success" @click="setToCart(element.id, element, -1)">-</button>
                </div>
                <input class="form-control text-center" type="number" readonly :value="cartElement.quantity">
                <div class="input-group-append">
                    <button class="btn btn-success" @click="addToCart(element)">+</button>
                </div>
            </div>
        </td>
        <td>
            <button class="btn btn-warning" @click="removeFromCart(element)">
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                    <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                    <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                </svg>
            </button>
        </td>
        <td>
            ${{ totalPrice }}
        </td>
    </tr>
</template>

<script>
    export default {
        props: ['element', 'cartElement'],
        computed: {
            totalPrice() {
                return this.cartElement.quantity * this.element.price
            }
        }
    }
</script>

