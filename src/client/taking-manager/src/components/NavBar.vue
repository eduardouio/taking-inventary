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
                <li 
                    v-for="(warenhouse, idx) in warenhouses" 
                    :key="warenhouse" 
                    class="list-group-item" 
                    @click="warenhouse.selected = !warenhouse.selected">
                  <span class="badge bg-secondary">
                      <i class="fas fa-minus text-danger"></i>
                      &nbsp;
                      Eliminar
                    </span>
                    &nbsp;
                    <span v-if="!warenhouse.selected" class="badge bg-danger">
                      Maracado Para Eliminar
                    </span>
                    <span v-if="!warenhouse.selected">&nbsp;</span>
                  <span class="badge bg-secondary">{{ idx + 1 }}</span> {{ warenhouse.name }}
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
                <button class="btn btn-outline-success btn-sm float-end" @click="updateWarenhouses">
              <i class="fa-solid fa-check"></i>
              Aplicar Cambios
            </button>
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
                  <tr 
                    v-for="(item, idx) in report.all_warenhouses" 
                    :key="item"
                    @click="item.selected = !item.selected"
                    >
                    <td class="text-center">
                      {{ idx + 1 }}
                    </td>
                    <td>{{ item.name }}</td>
                    <td class="text-center">
                      <span class="badge bg-secondary" v-if="!item.selected">
                        <i class="fas fa-plus text-success"></i>
                        Agregar
                      </span>
                      <span v-else class="badge bg-success">
                        Marcado Para Agregar
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      <!--/Vista Bodegas-->
      <!--Vista Grupos-->
      <div class="row" v-if="show_detail.groups">
        <div class="col-8">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title text-info">
                <i class="fa-solid fa-users"></i>
                Grupos
              </h5>
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
        <div class="col-4">
            <div class="card">
              <div class="card-header">
                <h5 class="card-title text-info">
                  <i class="fa-solid fa-user-plus"></i>
                  &nbsp;
                  Agregar Grupos
                  <button class="btn btn-outline-success btn-sm float-end" @click="addTeams">
                    <i class="fa-solid fa-check"></i>
                    Aplicar Cambios
                  </button>
                </h5>
              </div>
              <div class="card-body">
                  <input type="text" v-model="my_query" placeholder="Buscar" @keyup="filterUsers" class="float-end form-control form-control-sm ">
                  <table class="table table-hover table-bordered">
                    <thead>
                      <tr>
                        <th>#</th>
                        <th>Asistente</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(user,idx) in all_users_assistants" :key="user.id" @click="user.selected = !user.selected">
                        <td class="text-center">{{ idx+1 }}</td>
                        <td>
                          <span v-if="user.selected" class="badge bg-success">
                            &nbsp; Marcado Para Agregar
                          </span>
                          {{ user.first_name }} {{ user.last_name }}
                        </td>
                      </tr>
                    </tbody>
                  </table>
              </div>
            </div>
          </div>
      </div>
      <!--/Vista Grupos-->
    </div>
  </div>
</template>
<script>
export default {
  name: 'NavBar',
  emits: ['updateWarenhouses', 'updateGroups'],
  data() {
    return {
        show_detail: {
        enterprises: false,
        warenhouses: false,
        groups: false,
        },
      my_query:null,
      all_users_assistants: null
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
    },
    base_url: {
      type: String,
      required: true
    }
  }
  ,computed: {
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
    // filtramos usuarios del cuadro
    filterUsers() {
      this.all_users_assistants = this.report.all_users_assistants.map(item=>item)
      this.all_users_assistants = this.all_users_assistants.filter(
        user => {
          return user.first_name.toLowerCase().includes(this.my_query.toLowerCase()) ||
            user.last_name.toLowerCase().includes(this.my_query.toLowerCase())
        }
      )
    },
    // Actualizamos las bodegas
    updateWarenhouses() {
      this.$emit('updateWarenhouses');
  },
  // agregamos los grupos
  addTeams() {
    const teams = {
      'teams': this.all_users_assistants.filter(item => item.selected)
    } ;
    
    let xhr_team = new XMLHttpRequest();
    xhr_team.open(
      'POST', 
      this.base_url + '/api/common/add-team-taking/' + this.report.taking.id_taking + '/'
      );
    xhr_team.setRequestHeader('Content-Type', 'application/json');
    xhr_team.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr_team.onload = ()=>{
      if(xhr_team.status === 200){
        location.reload();
      }
    }
    xhr_team.send(JSON.stringify(teams));
    xhr_team.onerror = ()=>{
      alert('Error al agregar los grupos');
    }
  },//prox method

  },mounted(){
    this.all_users_assistants = this.report.all_users_assistants.map(item=>item);
  }
}
</script>

<style></style>