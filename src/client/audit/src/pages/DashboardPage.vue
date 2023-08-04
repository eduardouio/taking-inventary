<template>
    <div class="container-fluid">
        <NavBar class="bg-light border-bottom" :title="'Resumen Agosto'"/>
        <div class="row m-1"></div>
        <div class="row p-2">
            <div class="col border rounded m-1">
                <div class="row d-flex align-items-center">
                    <div class="col-3 text-center p-1">
                        <div class="bg-info bg-gradient text-center x-rounded align-bottom">
                            <h1 class="text-white p-1">35</h1>
                        </div>
                    </div>
                    <div class="col">
                        <span class="h4 text-secondary"><i class="fas fa-industry"></i>&nbsp;BODEGAS</span>
                    </div>
                </div>
            </div>
            <div class="col border rounded m-1">
                <div class="row d-flex align-items-center ">
                    <div class="col-3 text-center p-1">
                        <div class="bg-success bg-gradient text-center x-rounded align-bottom">
                            <h1 class="text-white p-1">32</h1>
                        </div>
                    </div>
                    <div class="col">
                        <span class="h4 text-secondary"><i class="fas fa-industry"></i>&nbsp;INVENTARIADAS</span>
                    </div>
                </div>
            </div>
            <div class="col border rounded m-1">
                <div class="row d-flex align-items-center ">
                    <div class="col-3 text-center p-1">
                        <div class="bg-warning bg-gradient text-center x-rounded align-bottom">
                            <h1 class="text-white p-1">3</h1>
                        </div>
                    </div>
                    <div class="col">
                        <span class="h4 text-secondary"><i class="fas fa-industry"></i>&nbsp;PENDIENTES</span>
                    </div>
                </div>
            </div>
            <div class="col border rounded m-1">
                <div class="row d-flex align-items-center ">
                    <div class="col-3 text-center p-1">
                        <div class="bg-danger bg-gradient text-center x-rounded align-bottom">
                            <h1 class="text-white p-1">55</h1>
                        </div>
                    </div>
                    <div class="col">
                        <span class="h4 text-secondary"><i class="fas fa-clipboard"></i>&nbsp;TOMAS FISICAS</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <div class="card bg-primary bg-gradient">
                    <span class="text-white">
                        TOMAS REALIZADAS
                    </span>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col table-responsive">
                <table class="table table-bordered table-striped table-hover">
                    <thead>
                        <tr class="text-center bg-success">
                            <th>#</th>
                            <th>Toma</th>
                            <th>Encargado</th>
                            <th>Empresas</th>
                            <th>Bodegas</th>
                            <th>Fecha</th>
                            <th>Inicio</th>
                            <th>Fin</th>
                            <th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Bodegas 10 de Agosto</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-success"><i class="fas fa-check"></i> Completo</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Ser Multimarc Bodegas Manta</td>
                            <td>Maria Briones</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:30</td>
                            <td class="text-end">15:00</td>
                            <td class="text-center text-primary"><i class="fas fa-check"></i> En Curso</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Bodegas Carcelen</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-success"><i class="fas fa-check"></i> Completo</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>La Guarda Cumbaya</td>
                            <td>Maria Fernanda</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">16:00</td>
                            <td class="text-center text-primary"><i class="fas fa-check"></i> En Curso</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Bodegas Vinesa 10 de Agosto</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-primary"><i class="fas fa-check"></i> En Curso</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Bodegas Vinesa 10 de Agosto</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-success"><i class="fas fa-check"></i> Completo</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Bodegas Vinesa 10 de Agosto</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-success"><i class="fas fa-check"></i> Completo</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Bodegas Vinesa 10 de Agosto</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-success"><i class="fas fa-check"></i> Completo</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Bodegas Vinesa 10 de Agosto</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-success"><i class="fas fa-check"></i> Completo</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>Bodegas Vinesa 10 de Agosto</td>
                            <td>Lorena Rodriguez</td>
                            <td class="text-center">3</td>
                            <td class="text-center">3</td>
                            <td>01/08/2023</td>
                            <td class="text-end">07:00</td>
                            <td class="text-end">13:00</td>
                            <td class="text-center text-success"><i class="fas fa-check"></i> Completo</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <TableComponent :key="1" :titleCard="'Bodegas'" :data="warenhouses" />
            </div>
            <div class="col">
                <TableComponent :key="2" :titleCard="'Empresas'" :data="owners"/>
            </div>
        </div>
        <span class="m-1"></span>
       
    </div>
</template>

<script>
//data table
import DataTable from 'datatables.net-dt';
import NavBar from '../components/NavBar.vue';
import TableComponent from '../components/TableComponent.vue';

export default {
    name: 'DashboardPage',
    components: {
        NavBar,
        TableComponent,
    }, methods: {
        startEnviroment() {
            console.log(DataTable);
        }
    },
    mounted() {
        this.startEnviroment();
    }, data() {
        return {
            warenhouses:
            {
                headers: [
                    { text: 'BODEGA', value: 'name' },
                    { text: 'INVENTARIADA', value: 'inventory' },
                    { text: 'ESTADO', value: 'status' },
                ], rows: [
                    { name: 'LAGUARDA MANTA', inventory: "COMPLETO", status: "complete" },
                    { name: 'LAGUARDA SAMBORONDON', inventory: "COMPLETO", status: "complete" },
                    { name: 'CONSIGNACIONES CLIENTES', inventory: "COMPLETO", status: "complete" },
                    { name: 'LAGUARDA LOS CEIBOS', inventory: "EN PROCESO", status: "complete" },
                    { name: 'LAGUARDA VIA LA COSTA', inventory: "COMPLETO", status: "complete" },
                    { name: 'MATRIZ PLUSBRAND MANTA', inventory: "COMPLETO", status: "complete" },
                    { name: 'MATRIZ PLUSBRAND GYE', inventory: "PENDIENTE", status: "complete" },
                    { name: 'LAGUARDA CUMBAYA', inventory: "COMPLETO", status: "complete" },
                    { name: 'ALMACEN 10 DE AGOSTO', inventory: "COMPLETO", status: "complete" },
                    { name: 'LAGUARDA', inventory: "COMPLETO", status: "complete" },
                    { name: 'LAGUARDA LOS CHILLOS', inventory: "PENDIENTE", status: "complete" },
                    { name: 'CONSIGNACIONES CLIENTES CUENCA', inventory: "COMPLETO", status: "complete" },
                    { name: 'LAGUARDA CUENCA', inventory: "COMPLETO", status: "complete" },
                    { name: 'MATRIZ PLUSBRAND CUENCA', inventory: "EN PROCESO", status: "complete" },
                    { name: 'LAGUARDA EL BOSQUE', inventory: "COMPLETO", status: "complete" },
                    { name: 'LAGUARDA PORTUGAL', inventory: "COMPLETO", status: "complete" },
                    { name: 'MATRIZ PLUSBRAND', inventory: "PENDIENTE", status: "complete" },
                    { name: 'BODEGA GENERAL G8', inventory: "PENDIENTE", status: "complete" },
                    { name: 'BODEGA CONSIGNACIONES CLIENTES', inventory: "PENDIENTE", status: "complete" },
                    { name: 'BODEGA CUENCA', inventory: "COMPLETO", status: "complete" },
                    { name: 'BODEGA CARCELEN', inventory: "COMPLETO", status: "complete" },
                    { name: 'ALMACÉN GENERAL UIO', inventory: "COMPLETO", status: "complete" },
                    { name: 'BODEGA CORDOVEZ CARCELEN', inventory: "COMPLETO", status: "complete" },
                    { name: 'VITRINA', inventory: "COMPLETO", status: "complete" },
                ],
            },
            owners: {
                headers: [
                    { text: 'EMPRESA', value: 'company' },
                    { text: 'BODEGAS', value: 'warenhouses' },
                    { text: 'INVENTARIADAS', value: 'inventory' },
                    { text: 'PENDIENTES', value: 'inventory' },
                    { text: 'ESTADO', value: 'status' }
                ], rows: [
                    { company: 'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.', warenhouses: 12, inventory: 10, pending: 2, status:"OK"},
                    { company: 'VIDINTERNACIONAL S.A.', warenhouses: 12, inventory: 10, pending: 2, status:"OK"},
                    { company: 'SERVICIOS MULTIMARCAS UNIDAS SERVMULTIMARC CIA LTDA', warenhouses: 12, inventory: 10, pending: 2, status:"OK"},
                    { company: 'CORPORACIÓN PLUSBRAND DEL ECUADOR CIA. LTDA.', warenhouses: 12, inventory: 10, pending: 2, status:"PENDIENTE"},
                    { company: 'VINOS Y ESPIRITUOSOS DEL LITORAL VINLITORAL S.A.', warenhouses: 12, inventory: 10, pending: 2, status:"OK"},
                    { company: 'VINOS Y ESPIRITUOSOS VINESA S.A', warenhouses: 12, inventory: 10, pending: 2, status:"PROCESO"},
                    { company: 'SERVICIOS MULTIMARCAS UNIDAS SERVMULTIMARC CIA LTDA', warenhouses: 12, inventory: 10, pending: 2, status:"OK"},
                    { company: 'CORPORACIÓN PLUSBRAND DEL ECUADOR CIA. LTDA.', warenhouses: 12, inventory: 10, pending: 2, status:"PENDIENTE"},
                    { company: 'VINOS Y ESPIRITUOSOS VINESA S.A', warenhouses: 12, inventory: 10, pending: 2, status:"OK"},
                ]
            },
        }
    },
}

</script>