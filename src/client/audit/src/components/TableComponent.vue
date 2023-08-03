<template>
    <div class="shadow">
        <div class="card-header text-center bg-secondary bg-gradient text-white rounded">
            {{ titleCard.toUpperCase() }}
        </div>
        <div class="table-responsive p-1">
    <table class="table table-condensed table-bordered table-striped table-hover" id="myTable">
        <thead>
            <tr>
                <th class="text-center" v-for="ite in data.headers" :key="ite">{{ ite.text }}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="row in data.rows" :key="row">
                <td v-for="column in row" :key="column">{{ column }}</td>
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
        }, data: {
            type: Array,
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
        return 0;
        let table = new DataTable('#myTable',{
            responsive: true,
            paging: true,
            showRowNumber: true,
        });
    },
}
</script>
<style scoped>
.table-responsive{
    max-height: 16rem;
    min-height: 16rem;
}
</style>