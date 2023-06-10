<template>
    <div class="bg-light">
        <div class="container-fluid mt-3" v-if="show_view_report">
            <table class="table table-hover table-bordered" id="report">
                <thead>
                        <tr class="bg-secondary text-white">
                            <th class="text-center">#</th>
                            <th class="text-center text-nowrap">Producto</th>
                            <th class="text-center">SKU</th>
                            <th class="text-center">Capacidad</th>
                            <th class="text-center">CxCaja</th>
                            <th class="text-center">Stock</th>
                            <th class="text-center">Toma</th>
                            <th class="text-center">Diff</th>
                            <th class="text-center">Status</th>
                        </tr>
                </thead>
                <tbody>
                    <tr v-for="( item, index) in table_takings" :key="item" @click="showItemDetail(item)">
                       <td class="text-center">{{ index + 1 }}</td>
                       <td>{{ item.product.name }}</td>
                       <td>{{ item.product.ean_13_code }}</td>
                       <td class="text-end">{{ item.product.capacity }}</td>
                       <td class="text-end">{{ item.product.quantity_per_box }}</td>
                       <td class="text-end">{{ item.sap_stock }}</td>
                       <td class="text-end">{{ item.tk_quantity }}</td>
                       <td class="text-end">{{ item.sap_stock - item.tk_quantity }}</td>
                       <td class="text-center text-success" v-if="item.sap_stock === item.tk_quantity">COMPLETO</td>
                       <td class="text-center text-danger" v-if="item.sap_stock < item.tk_quantity">SOBRANTE</td>
                       <td class="text-center" v-if="item.sap_stock > item.tk_quantity">
                            <span v-if="item.tk_quantity === 0" class="text-info">SIN TOMA</span>
                            <span v-else class="text-danger">FALTANTE</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div v-else>
            <base-detail
                :selected_item="selected_item"
                :show_view_report="show_view_report"
                :base_url="base_url"
                :report="report"
                :taking_is_open ="taking_is_open"
                :csrf_token="csrf_token"
                @showReport="showReport"
                @makeRecount="makeRecount($event)"
                ></base-detail>
        </div>
    </div>
</template>
<script>
import $ from 'jquery';
import DataTable from 'datatables.net-dt';
import 'datatables.net-dt/css/jquery.dataTables.css';
import BaseDetail from './BaseDetail.vue';

window.$ = $;
window.jQuery = $;

export default {
    name: 'TakingReport',
    emits: ['makeRecount'],
    props: {
        table_takings: {
            type: Object,
            required: true,
        },
        base_url: {
            type: String,
            required: true,
        },
        show_all_takings: {
            type: Boolean,
            required: true,
        },report: {
            type: Object,
            required: true,
        }, taking_is_open: {
            type: Boolean,
            required: true,
        },csrf_token: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            selected_item: null,
            show_view_report:true,
            datatable: null,
        }
    },
    methods: {
        // muestra el detalle de la toma seleccionada
        showItemDetail(item) {
            this.show_view_report = false;
            this.selected_item = item;
        },showReport() {
            this.show_view_report = true;
            this.$nextTick(() => {
                this.initDataTable();
            });
        }, makeRecount(account_code) {
            this.$emit('makeRecount', account_code);
        },initDataTable(){
            // comprobamos si ya existe una instancia de DataTable
            if (this.datatable !== null) {
                this.datatable.destroy();
                this.datatable = null;
            }

            // creamos una nueva instancia de DataTable
            this.dataTable = new DataTable("#report",{
                pageLength: 25,
                lengthMenu: [ 10, 25, 50, 75, 100, 200, 500, 1000,],
                language: {
                    url: "//cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json"
                },
            });
        },//next_method
    },components: {
        BaseDetail,
    },watch:{
        show_view_report(){
            if(this.show_view_report){
                this.initDataTable();
            }
     },
    },mounted(){
        this.$nextTick(() => {
            this.initDataTable();
        });
    }
}
</script>

<style>
    table tbody th, tbody td {
        padding: 0.6px 1px !important;
        border: 0.1px solid #ddd !important;
    }
    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }
</style>