<template>
<div>
  <div class="flex flex-col h-screen">
    <nav class="bg-gray-800 text-white px-4 py-3">
      <h1 class="text-lg font-bold">Dashboard</h1>
    </nav>
    <main class="flex-1 p-4">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div class="bg-white rounded-lg shadow-md p-4">
          <h2 class="text-lg font-bold mb-2">Users</h2>
          <p class="text-gray-700">Total users: 100</p>
        </div>
        <div class="bg-white rounded-lg shadow-md p-4">
          <h2 class="text-lg font-bold mb-2">Sales</h2>
          <p class="text-gray-700">Total sales: $10,000</p>
        </div>
        <div class="bg-white rounded-lg shadow-md p-4">
          <h2 class="text-lg font-bold mb-2">Orders</h2>
          <p class="text-gray-700">Total orders: 50</p>
        </div>
      </div>
    </main>
    <footer class="bg-gray-800 text-white px-4 py-3">
      <p>&copy; 2021 My Company</p>
    </footer>
  </div>
</div>
</template>

<script>
//data table
//import DataTable from 'datatables.net-dt';
//import NavBar from '../components/NavBar.vue';
//import TableComponent from '../components/TableComponent.vue';

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