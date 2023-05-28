<template>
  <div class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">TOMA # <span v-if="report" v-text="report.taking.id_taking"></span></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a href="/" class="nav-link">
                Inicio
              </a>
            </li>
            <li class="nav-item" @click="showDetail('enterprises')">
              <span class="nav-link">
                Empresas &nbsp;
                <span class="badge rounded-pill bg-info text-dark" v-if="report.enterprises.length"> {{
                  report.enterprises.length }}</span>
                <span class="badge rounded-pill bg-info text-dark" v-else> Error </span>
              </span>
            </li>
            <li class="nav-item" @click="showDetail('warenhouses')">
              <span class="nav-link">Bodegas &nbsp;
                <span class="badge rounded-pill bg-info text-dark" v-if="warenhouses.length"> {{ warenhouses.length
                }}</span>
              </span>
            </li>
            <li class="nav-item" @click="showDetail('groups')">
              <span class="nav-link">Grupos &nbsp;
                <span class="badge rounded-pill bg-info text-dark" v-if="report.teams.length"> {{ report.teams.length
                }}</span>
              </span>
            </li>
          </ul>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Pendientes:
                </span>
                <strong class="badge bg-danger text-dark">{{ left_over }}</strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Completos:
                </span><strong class="badge bg-success"> {{ full }} / {{ report.report.length }} </strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link">
                <span class="text-white">
                  Progreso:
                </span>
                <strong class="text-light badge bg-primary">
                  {{ percent_progress }}%
                </strong>
              </span>
            </li>
          </ul>
          <span class="nav-div">&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <i class="fas fa-user text-secondary"></i>
              &nbsp;
              <span class="navbar-text">
                {{ userdata.first_name }} {{ userdata.last_name }}
                &nbsp;
                <a href="/accounts/logout/">
                  <i class="fas fa-power-off text-danger"></i>
                </a>
              </span>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container-fluid">
      <!--Vista Empresas-->
      <div class="row" v-if="show_detail.enterprises">
        <div class="col-4">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title text-info">Empresas</h5>
            </div>
            <div class="card-body">
              <h6 class="card-subtitle mb-2 text-muted">Listado de Propietarios</h6>
              <ul class="list-group">
                <li v-for="(enterprise, idx) in report.enterprises" :key="enterprise" class="list-group-item">
                  <span class="badge bg-secondary">{{ idx + 1 }}</span> {{ enterprise }}
                </li>
              </ul>
              <button class="btn btn-sm btn-outline-dark mt-2" @click="showDetail">
                <i class="fas fa-xmark"></i> Cerrar
              </button>
            </div>
          </div>
        </div>
      </div>
      <!--/Vista Empresas-->
      <!--Vista Bodegas-->
      <div class="row" v-if="show_detail.warenhouses">
        <div class="col-4">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title text-info">
                <i class="fa-solid fa-warehouse"></i>
                Bodegas
              </h5>
            </div>
            <div class="card-body">
              <h6 class="card-subtitle mb-2 text-muted">Listado de Bodegas</h6>
              <ul class="list-group">
                <li v-for="(warenhouse, idx) in warenhouses" :key="warenhouse" class="list-group-item">
                  <span class="badge bg-secondary">
                      <i class="fas fa-minus text-danger"></i>
                      &nbsp;
                      Eliminar
                    </span>
                    &nbsp;
                  <span class="badge bg-secondary">{{ idx + 1 }}</span> {{ warenhouse }}
                </li>
              </ul>
              <button class="btn btn-sm btn-outline-dark mt-2" @click="showDetail">
                <i class="fas fa-xmark"></i> Cerrar
              </button>
              &nbsp;
            </div>
          </div>
        </div>
        <div class="col-4">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title text-info">
                <i class="fa-solid fa-plus"></i>
                &nbsp;
                Agregar Bodegas
              </h5>
            </div>
            <div class="card-body">
              <table id="table-whrs" class="table table-bordered table-hover">
                <thead>
                  <tr class="text-center">
                    <th>#</th>
                    <th>Bodega</th>
                    <th><i class="fas fa-gears"></i></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, idx) in report.all_warenhouses" :key="item">
                    <td class="text-center">
                      {{ idx + 1 }}
                    </td>
                    <td>{{ item.name }}</td>
                    <td class="text-center">
                      <span class="badge bg-secondary">
                        <i class="fas fa-plus text-success"></i>
                        Agregar
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="col-2">
          <button class="btn btn-outline-success">
            <i class="fa-solid fa-check"></i>
            Aplicar Cambios
          </button>
        </div>
      </div>
      <!--/Vista Bodegas-->
      <!--Vista Grupos-->
      <div class="row" v-if="show_detail.groups">
        <div class="col">
          <div class="card" style="width: 100rem;">
            <div class="card-header">
              <h5 class="card-title text-info">Grupos</h5>
            </div>
            <div class="card-body">
              <h6 class="card-subtitle mb-2 text-muted">Listado de Grupos</h6>
              <table class="table table-hover table-bordered">
                <thead>
                  <tr class="text-center">
                    <th>Grupo</th>
                    <th>Manager</th>
                    <th>Asistente</th>
                    <th><i class="fas fa-refresh"></i></th>
                    <th>Ultima</th>
                    <th><i class="fas fa-gears"></i></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="team in report.teams" :key="team">
                    <td class="text-center">{{ team.group_number }}</td>
                    <td>{{ team.manager.first_name }} {{ team.manager.last_name }}</td>
                    <td>{{ team.warenhouse_assistant }}</td>
                    <td class="text-center">{{ team.activity.count }}</td>
                    <td>
                      <span v-if="team.activity.last_taking">
                        {{ new Date(team.activity.last_taking).toLocaleString('es-Ec') }}
                      </span>
                      <span v-else class="text-danger">No tiene</span>
                    </td>
                    <td class="text-center">
                      <span v-if="team.activity.last_taking" class="text-secondary">
                        <i class="fas fa-stop"></i>
                      </span>
                      <span v-else class="text-danger" data-bs-toggle="tooltip" data-bs-placement="top"
                        title="Elimnar Grupo">
                        [<i class="fas fa-minus"></i>]
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
              <button class="btn btn-sm btn-outline-dark mt-2" @click="showDetail">
                <i class="fas fa-xmark"></i> Cerrar
              </button>
              &nbsp;
              <button class="btn btn-sm btn-outline-primary mt-2">
                <i class="fas fa-user-plus"></i>
                Agregar Grupo
              </button>
            </div>
          </div>
        </div>
      </div>
      <!--/Vista Grupos-->
    </div>
  </div>
</template>
<script>
import DataTable from 'datatables.net-dt';
import 'datatables.net-dt/css/jquery.dataTables.css';

export default {
  name: 'NavBar',
  data() {
    return {
      show_detail: {
        enterprises: false,
        warenhouses: false,
        groups: false,
      }
    }
  },
  props: {
    report: {
      type: Object,
      required: true
    }, warenhouses: {
      type: Array,
      required: true
    }, userdata: {
      type: Object,
      required: true
    }
  }, computed: {
    // items completos
    full() {
      return this.report.report.filter(
        item => item.is_complete == true
      ).length;
    }, left_over() {
      return this.report.report.filter(
        item => item.is_complete == false
      ).length;
    }, percent_progress() {
      return Math.round((this.full / this.report.report.length) * 100);
    }
  }, methods: {
    // Mostramos u ocultamos las vistas de empresas, bodegas y grupos
    showDetail(name = null) {
      this.show_detail = {
        enterprises: false,
        warenhouses: false,
        groups: false,
      };
      if (name === null) {
        return
      }
      this.show_detail[name] = true;
    },
    // eliminamos una bodega de la toma
    deleteWarenhouse(name){

    },
    //agregamos una bodega a la toma
    addWarenhouses(){
      
    },
  }, mounted() {
    let my_table = new DataTable("#table-whrs", {
      pageLength: 20,
      lengthMenu: [[20, 50, 100, -1], ["20", "50", "100", "Todos"]],
    })
  }
}
</script>

<style></style>