<template>
    <div class="card">
        <div class="card-header text-center bg-secondary bg-gradient text-white">
            {{ titleCard.toUpperCase() }}
        </div>
        <div class="card-body">
    <table class="table table-condensed table-bordered table-striped table-hover" id="myTable">
        <thead>
            <tr>
                <th class="text-center">Id</th>
                <th class="text-center">Nombre</th>
                <th class="text-center">Toma</th>
                <th class="text-center">Fecha</th>
                <th class="text-center">Novedades</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in range(10)" :key="item">
                <td>1</td>
                <td>Almacen 1</td>
                <td>1</td>
                <td>2021-08-01</td>
                <td>0</td>
            </tr>
        </tbody>
    </table>
</div>
</div>
</template>
<script>
/* eslint-disable */
import DataTable from 'datatables.net-dt'

export default {
    name: 'TableComponent',
    props: {
        titleCard: {
            type: String,
            required: true,
        }
    },
    data() {
        return {
            table: null,
        }
    },
    methods: {
        range(n) {
            return [...Array(n).keys()]
        },
    },
    created() {
        let table = new DataTable('#myTable',{
            responsive: true,
            paging: true,
            showRowNumber: true,
        });
    },
}
</script>