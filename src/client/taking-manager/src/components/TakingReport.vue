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
                    <tr v-for="( item, index) in report.report" :key="item.prod" @click="showItemDetail(item)">
                       <td class="text-center">{{ index + 1 }}</td>
                       <td>{{ item.product.name }}</td>
                       <td>{{ item.product.ean_13_code }}</td>
                       <td class="text-end">{{ item.product.capacity }}</td>
                       <td class="text-end">{{ item.product.quantity_per_box }}</td>
                       <td class="text-end">{{ item.sap_stock }}</td>
                       <td class="text-end">{{ item.quantity }}</td>
                       <td class="text-end">{{ item.sap_stock - item.quantity }}</td>
                       <td class="text-center text-success" v-if="item.sap_stock === item.quantity">COMPLETO</td>
                       <td class="text-center text-danger" v-if="item.sap_stock < item.quantity">SOBRANTE</td>
                       <td class="text-center" v-if="item.sap_stock > item.quantity">
                            <span v-if="item.quantity === 0" class="text-info">SIN TOMA</span>
                            <span v-else class="text-danger">FALTANTE</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div v-else>
            <base-detail
                :selected_item="selected_item"
                @showReport="showReport"
                :show_view_report="show_view_report"
                :base_url="base_url"
                :report="report"
                ></base-detail>
        </div>
    </div>
</template>
<script>

import DataTable from 'datatables.net-dt';
import 'datatables.net-dt/css/jquery.dataTables.css';
import BaseDetail from './BaseDetail.vue';

export default {
    name: 'TakingReport',
    props: {
        report: {
            type: Object,
            required: true,
        },
        base_url: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            selected_item: null,
            show_view_report:true,
        }
    },
    methods: {
        showItemDetail(item) {
            this.show_view_report = false;
            this.selected_item = item;
        },showReport() {
            this.show_view_report = true;
            this.initializeDataTable();
        }, initializeDataTable() {
            if (!this.data) {
                this.data = new DataTable("#report", {
                    pageLength: 20,
                    lengthMenu: [[20, 50, 100, -1], ["20", "50", "100", "Todos"]],
                });
            } else {
                this.data.clear().destroy();
                this.data = new DataTable("#report", {
                    pageLength: 20,
                    lengthMenu: [[20, 50, 100, -1], ["20", "50", "100", "Todos"]],
                });
            }
        },
       destroyDataTable() {
            if (this.data) {
                this.data.clear().destroy();
                this.data = null;
            }
        },
    },
    computed: {
    },
    mounted() {
        this.initializeDataTable();
    },beforeUnmount() {
        this.destroyDataTable();
    },
    components: {
        BaseDetail,
    },

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