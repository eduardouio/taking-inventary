<template>
     <div class="card card-outline card-info">
                <div class="card-header">
                    <div id="header" if="show_search">
                        <div class="row">
                            <div class="col text-center">
                                <i class="fas fa-search"></i>
                                <strong class="text-info">Buscar Producto</strong>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <input type="text" class="form-control" v-model="query_search" @keyup="searchList">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                Resultados:
                                <strong class="text-primary" v-text="query_search"></strong>
                                &nbsp;
                                <span class="text-info" v-if="filtered_products">
                                    <span v-text="filtered_products.length"></span> 
                                    registros encontrados de {{ products.length }}
                                </span>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <ul class="list-group" v-for="(product, index) in filtered_products">
                                    <li class="list-group-item bg-gradient-light" @click="selectProduct(product)">
                                        <small class="text-secondary" v-text="product.fields.name">
                                        </small>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
</template>
<script>
export default{
    name: 'SearchForm',
    props: ['products'],
    emits: ['select-product'],
    data(){
        return{
            query_search: '',
            filtered_products: [],
            show_search: true,
        }
    },methods: {
        searchList() {
            if (this.query_search.length < 3) {
                return false;
            }
            let params = this.query_search.toUpperCase().split(' ');
            this.filtered_products = this.products.filter(function (elm) {
                let condition = true;
                for (let i = 0; i < params.length; i++) {
                    if (elm.fields.name.search(params[i]) < 0) {
                        condition = false;
                    }
                }
                return condition;
            }).slice(0, 20);
        },
        selectProduct(product) {
            this.$emit('selectproduct', product);
        },
    }
}
</script>