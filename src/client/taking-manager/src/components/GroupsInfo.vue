<template>
  <div>
    <div class="container-fluid mt-3">
      <div class="row">
        <div class="col">
          <table class="table table-bordered table-hover" id="group-info">
            <thead>
              <tr class="bg-primary text-white">
                <th class="text-center">#</th>
                <th class="text-center"><i class="fas fa-user"></i></th>
                <th class="text-center">Auxiliar</th>
                <th class="text-center"><i class="fas fa-refresh"></i></th>
                <th class="text-center"><i class="fas fa-clock"></i></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center">1</td>
                <td>Eduardo Villota</td>
                <td>Afredo Caamanero</td>
                <td class="text-center"><label for="" class="badge bg-success">21</label></td>
                <td>12 de Febrero a las 09:00</td>
              </tr>
              <tr>
                <td class="text-center">2</td>
                <td>Carlos Villota</td>
                <td>Carlos Caamanero</td>
                <td class="text-center"><label for="" class="badge bg-success">21</label></td>
                <td>12 de Febrero a las 09:00</td>
              </tr>
              <tr>
                <td class="text-center">3</td>
                <td>Carlos Villota</td>
                <td>Carlos Caamanero</td>
                <td class="text-center"><label for="" class="badge bg-success">21</label></td>
                <td>12 de Febrero a las 09:00</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col">
          <table class="table table-bordered table-hover">
            <thead>
              <tr class="bg-secondary">
                <th>#</th>
                <th>Producto</th>
                <th>Toma</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>Porducto en mejor de todos</td>
                <td>423</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import DataTable from 'datatables.net-dt';
import 'datatables.net-dt/css/jquery.dataTables.css';

export default {
  name: "GroupsInfo",
  data: function () {
    return {
      "data": "Genial",
    }
  },
  methods: {
    "updateData": function () {
      this.data = [];
    }
  },
  mounted: function () {
    let x = new DataTable("#group-info", {
      pageLength: -1,
      lengthMenu: [[20, 50, 100, -1], ["20", "50", "100", "Todos"]],
      searching: false,
      paging: false,
    })
  },
}
</script>