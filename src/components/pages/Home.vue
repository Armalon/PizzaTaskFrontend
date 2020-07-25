<template>
    <div>
        <div class="px-3 py-3 pb-md-4 mx-auto text-center">
            <h1 class="display-4">Menu</h1>
            <p class="lead">
                Our delicious pizza will not leave you indifferent
            </p>
        </div>

        <div class="container">
            <span class="h3">Search filters</span>
            <search-filters
                    @souseBaseChange="souseBaseChange($event)"
                    @pizzaCrustChange="pizzaCrustChange($event)"></search-filters>

            <loader v-if="menuList == null"></loader>

            <div class="card-columns mb-3 text-center" v-if="menuList != null">
                <menu-element
                        v-for="menuElement in filteredMenuPizzaList"
                        :element="menuElement"
                        :key="menuElement.id">
                </menu-element>
            </div>

            <div class="h3 mb-2">We recommend drinks</div>
            <div class="card-columns mb-3 text-center" v-if="menuDrinkList != null">
                <menu-element
                        v-for="menuElement in menuDrinkList"
                        :element="menuElement"
                        :key="menuElement.id">
                </menu-element>
            </div>
        </div>

    </div>
</template>

<script>
    import SearchFilters from "../SearchFilters";
    import MenuElement from "../MenuElement";

    export default {
        data() {
            return {
                menuList: null,
                filters: {
                    souse_base: 'any',
                    pizza_crust: 'any',
                }
            }
        },
        methods: {
            authorizeMe() {
                this.axios.get('/login', { withCredentials: true }).then((response) => {
                    if (response.data
                        && !response.data.error
                        && response.data.user) {

                        this.$store.dispatch('setIAmAuthorized', response.data.user);
                    }
                })
            },
            loggingMeOut() {
                this.axios.get('/logout', { withCredentials: true }).then((response) => {
                    if (response.data
                        && !response.data.error) {

                        this.$store.dispatch('setIAmAuthorized', null);
                    }
                })
            },
            souseBaseChange(val) {
                this.filters.souse_base = val
            },
            pizzaCrustChange(val) {
                this.filters.pizza_crust = val
            },
        },
        computed: {
            menuPizzaList() {
                return this.menuList ? this.menuList.filter(product => product.type == 'PIZZA') : []
            },
            filteredMenuPizzaList() {
                return this.menuPizzaList.filter(product => {
                    for (let key in this.filters) {
                        if (this.filters[key] !== 'any') {
                            if (key === 'souse_base' && product.base.toLowerCase() !== this.filters[key]) {
                                return false;
                            }
                            if (key === 'pizza_crust' && product.crust.toLowerCase() !== this.filters[key]) {
                                return false;
                            }
                        }
                    }

                    return true;
                })
            },
            menuDrinkList() {
                return this.menuList ? this.menuList.filter(product => product.type == 'DRINK') : []
            },
        },
        created() {
            this.axios.get('/menu', { withCredentials: true }).then((response) => {
                if (response.data
                    && !response.data.error
                    && response.data.products) {

                    this.menuList = response.data.products;
                }
            })
        },
        components: {
            SearchFilters,
            MenuElement
        },
    }
</script>