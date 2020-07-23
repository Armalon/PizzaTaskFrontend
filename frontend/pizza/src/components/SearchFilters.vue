<template>
    <div class="row mb-4 border pb-4 pt-2">
        <div class="col-sm-6">
            Pizza souse base:
            <br>

            <div class="btn-group btn-group-toggle">
                <label class="btn btn-success" :class="{ active: souse_base === 'any', 'font-weight-bold': souse_base === 'any' }">
                    <input type="radio" v-model="souse_base" name="souse_base" value="any">Any
                </label>
                <label class="btn btn-danger" :class="{ active: souse_base === 'red', 'font-weight-bold': souse_base === 'red' }">
                    <input type="radio" v-model="souse_base" name="souse_base" value="red"> Red tomato
                </label>
                <label class="btn btn-light" :class="{ active: souse_base === 'white', 'font-weight-bold': souse_base === 'white' }">
                    <input type="radio" v-model="souse_base" name="souse_base" value="white"> White
                </label>
            </div>

        </div>
        <div class="col-sm-6">
            Pizza Crust:
            <br>

            <div class="btn-group btn-group-toggle">
                <label class="btn btn-success" :class="{ active: pizza_crust === 'any', 'font-weight-bold': pizza_crust === 'any' }">
                    <input type="radio" v-model="pizza_crust" name="pizza_crust" value="any" checked>Any
                </label>
                <label class="btn btn-light" :class="{ active: pizza_crust === 'thin', 'font-weight-bold': pizza_crust === 'thin' }">
                    <input type="radio" v-model="pizza_crust" name="pizza_crust" value="thin"> Thin
                </label>
                <label class="btn btn-warning" :class="{ active: pizza_crust === 'thick', 'font-weight-bold': pizza_crust === 'thick' }">
                    <input type="radio" v-model="pizza_crust" name="pizza_crust" value="thick"> Thick
                </label>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                souse_base: 'any',
                pizza_crust: 'any',
            }
        },
        watch: {
            souse_base(value) {
                this.$emit('souseBaseChange', value)
            },
            pizza_crust(value) {
                this.$emit('pizzaCrustChange', value)
            },
        }
    }
</script>