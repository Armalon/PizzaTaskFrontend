<template>
    <div class="row mb-4 border pb-4 pt-2">
        <div class="col-sm-6">
            Pizza souse base:
            <br>

            <div class="btn-group btn-group-toggle" data-toggle="buttons">
                <label class="btn btn-success active font-weight-bold">
                    <input type="radio" name="souse_base" value="any" checked>Any
                </label>
                <label class="btn btn-danger">
                    <input type="radio" name="souse_base" value="red"> Red tomato
                </label>
                <label class="btn btn-light">
                    <input type="radio" name="souse_base" value="white"> White with garlic
                </label>
            </div>

        </div>
        <div class="col-sm-6">
            Pizza Crust:
            <br>

            <div class="btn-group btn-group-toggle" data-toggle="buttons">
                <label class="btn btn-success active font-weight-bold">
                    <input type="radio" name="crust" value="any" checked>Any
                </label>
                <label class="btn btn-light">
                    <input type="radio" name="crust" value="red"> Thin
                </label>
                <label class="btn btn-warning">
                    <input type="radio" name="crust" value="white"> Thick
                </label>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
    }
</script>