<template>
    <div class="container-fluid">
        <NavBar class="bg-light border-bottom"/>
        <div class="row m-1"></div>
        <div class="row">
            <div class="col-xl-3 text-center border">
                                <div class="text-white">
                                    <div class="bg-secondary bg-gradient text-center x-rounded shadow">
                                        <h1>5</h1> Bodegas
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-3 text-center border">
                                <div class="text-white">
                                    <div class="bg-secondary bg-gradient text-center x-rounded shadow">
                                        <h1>5</h1> Bodegas
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-3 text-center border">
                                <div class="text-white">
                                    <div class="bg-secondary bg-gradient text-center x-rounded shadow">
                                        <h1>5</h1> Bodegas
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-3 text-center border">
                                <div class="text-white">
                                    <div class="bg-secondary bg-gradient text-center x-rounded shadow">
                                        <h1>5</h1> Bodegas
                                    </div>
                                </div>
                            </div>
                         
                        </div>
        <div class="row">
            <div class="col">
                <TableComponent :key="1" :titleCard="'Bodegas'"/>
            </div>
            <div class="col">
                <TableComponent :key="2" :titleCard="'Empresas'"/>
            </div>
        </div>
    </div>
</template>

<script>
//data table
import DataTable from 'datatables.net-dt';
import NavBar from '../components/NavBar.vue';
import TableComponent from '../components/TableComponent.vue';

export default {
        name: 'AuditPage',
        components: {
            NavBar,
            TableComponent,
        },methods:{
            startEnviroment(){
                console.log(DataTable);
            }
        },
        mounted(){
            this.startEnviroment();
        }
    }

</script>