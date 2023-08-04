<template>
    <div class="card card-outline card-info">
        <div class="card-header">
            <div id="header">
                <div class="row mt-1" v-if="false">
                    <div class="col">
                        <button
                            type="button"
                            class="btn bordered" 
                            @click="$event => show_barcode_reader = false">
                            <i class="fas fa-search"></i>
                            <span class="text-info"> Buscar</span>
                        </button>
                    </div>
                    <div class="col text-end">
                            <button class="btn bordered" @click="$event=>show_barcode_reader = true">
                            <i class="fas fa-barcode"></i>
                            <span class="text-info"> Escanear</span>
                        </button>
                        </div>
                </div>
                <div class="row mt-1" v-if="show_barcode_reader">
                    <div class="col">
                        <barcode-reader
                            v-if="show_barcode_reader"
                            @ean_code="$event => selectByBarcode($event)"
                        ></barcode-reader>
                    </div>
                </div>
                <div class="row mt-1" v-if="show_text_search">
                        <div class="col">
                            <input type="text" class="form-control" v-model="query_search" @keyup="searchList">
                        </div>
                    </div>
                <div class="row">
                    <div class="col">
                        <small>Resultados: </small>
                        <small class="text-primary" v-text="query_search"></small>
                        <small class="text-secondary" v-if="filtered_products">
                            <small v-text="filtered_products.length"></small>
                             registros encontrados de {{ products.length }}
                        </small>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <ul class="list-group" :key=index v-for="(product, index) in filtered_products">
                            <li class="list-group-item bg-gradient-light" @click="$event => selectProduct(product)">
                                <small class="text-secondary" v-text="product.name">
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
import BarcodeReader from './BarcodeReader.vue';

export default{
    name: 'SearchForm',
    props: ['products'],
    emits: ['selectProduct'],
    data(){
        return{
            query_search: '',
            filtered_products: [],
            show_text_search: true,
            show_barcode_reader: false,
        }
    },methods: {
        searchList() {
            if (this.query_search.length < 3) {
                return false;
            }
            const self = this;
            // buscamos por nombre en los productos
            let params = this.query_search.toUpperCase().split(' ');
            let filtered_by_name = this.products.filter(function (elm) {
                let condition = true;
                for (let i = 0; i < params.length; i++) {
                    if (elm.name.search(params[i]) < 0) {
                        condition = false;
                    }
                }
                return condition;
            }).slice(0, 20);

            // buscamos por código de barras
            let filtered_by_barcode = this.products.filter(
                function (elm) {
                    if (elm.ean_13_code === null) {
                        return false;
                    }
                    return elm.ean_13_code.includes(self.query_search);
                }
            ).slice(0, 20);

            // unimos los resultados
            this.filtered_products = filtered_by_name.concat(
                filtered_by_barcode
            );
        },
        selectProduct(product) {
            this.$emit('selectProduct', product);
            this.show_barcode_reader=false;
        },
        selectByBarcode(barcode){
            this.query_search = barcode;
            this.show_barcode_reader = false;
            this.show_text_search = true;
            this.searchList();
        }
    },
    components: {
        BarcodeReader,
    }
}
</script>