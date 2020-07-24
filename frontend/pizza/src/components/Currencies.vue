<template>
    <div class="my-2 mx-2 ml-md-auto ">
        <div class="btn-group btn-group-toggle">
            <label class="btn btn-success" :class="{ active: currency === 'usd', 'font-weight-bold': currency === 'usd' }">
                <input type="radio" name="currency" value="usd" v-model="currency">USD
            </label>
            <label class="btn btn-info" :class="{ active: currency === 'eur', 'font-weight-bold': currency === 'eur' }">
                <input type="radio" name="currency" value="eur" v-model="currency">EUR
            </label>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                currency: null
            }
        },
        watch: {
            currency(val) {
                this.$store.dispatch('setCurrency', val)
            }
        },
        computed: {
        },
        created() {
            this.currency = this.globalCurrency
        }
    }
</script>