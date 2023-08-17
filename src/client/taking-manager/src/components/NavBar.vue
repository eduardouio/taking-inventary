<template>
  <div class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container-fluid">
        <a class="navbar-brand text-primary" href="#"> 
            [T-<span v-if="taking" v-text="taking.id_taking"></span>]
            {{ taking.name}}
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a href="/" class="nav-link">
                <i class="fa-solid fa-home"></i>
                Inicio
              </a>
            </li>
              <li class="nav-item">
                <a href="/sap/" class="nav-link">
                  <i class="fa-solid fa-server"></i>
                  Saldos SAP
                </a>
              </li>
              <li class="nav-item">
                <a href="/takings/" class="nav-link">
                  <i class="fa-solid fa-list-check"></i>
                  Tomas
                </a>
              </li>
              <li>
                &nbsp;
              </li>
            <li class="nav-item" @click="showDetail('enterprises')">
              <span class="nav-link">
                Empresas &nbsp;
                <span class="badge rounded-pill bg-info text-dark" v-if="allEnterprises"> {{
                  allEnterprises.length }}</span>
                <span class="badge rounded-pill bg-info text-dark" v-else> Error </span>
              </span>
            </li>
            <li class="nav-item" @click="showDetail('warenhouses')">
              <span class="nav-link">Bodegas &nbsp;
                <span class="badge rounded-pill bg-info text-dark" v-if="allWarenhouses.length"> {{ allWarenhouses.length
                }}</span>
              </span>
            </li>
            <li class="nav-item" @click="showDetail('groups')">
              <span class="nav-link">Grupos &nbsp;
                <span class="badge rounded-pill bg-info text-dark" v-if="taking.teams.length">
                {{ taking.teams.length}}
                </span>
              </span>
            </li>
          </ul>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <span class="nav-link"><span>
                <small>
                  Pendientes:
                </small>
                </span>
                <strong class="badge bg-danger text-dark">{{ left_over }}</strong></span>
            </li>
            &nbsp;
            <li class="nav-item">
              <span class="nav-link"><span>
                <small>
                  Completos:
                </small>
                </span><strong class="badge bg-success"> {{ full }} / {{ reportTaking.length }} </strong></span>
            </li>
              &nbsp;
            <li class="nav-item">
              <span class="nav-link">
                <small>
                  Progreso:
                </small>
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
                <small class="bnavbar-brand">
                  {{ userManager.username }}
                </small>
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
      <div class="row" v-if="showSection.enterprises" >
        <div class="col-4">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title text-info">
              <i class="fas fa-house"></i>
                Empresas Seleccionadas
              </h5>
            </div>
            <div class="card-body">
              <ul class="list-group">
                <li v-for="(enterprise, idx) in allEnterprises" :key="enterprise" class="list-group-item">
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
       <div class="row" v-if="showSection.warenhouses">
        <div class="col-4">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title text-success">
                <i class="fa-solid fa-warehouse"></i>
                Bodegas Seleccionadas
              </h5>
            </div>
            <div class="card-body">
              <ul class="list-group">
                <li 
                    v-for="(warenhouse, idx) in allWarenhousesSelected" 
                    :key="warenhouse" 
                    class="list-group-item" 
                    @click="warenhouse.selected = !warenhouse.selected"
                    >
                    <span class="badge bg-success bg-gradient">{{ idx + 1 }}</span> 
                    &nbsp;
                  <span class="badge bg-light bg-gradient bordered text-danger">
                      <i class="fas fa-minus text-danger"></i>
                      &nbsp;
                      Eliminar
                    </span>
                  {{ warenhouse.name }}
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
                    v-for="(item, idx) in allWarenhousesUnseleted" 
                    :key="item"
                    @click="item.selected = !item.selected"
                    >
                    <td class="text-center">
                      {{ idx + 1 }}
                    </td>
                    <td>{{ item.name }}</td>
                    <td class="text-center">
                      <span class="badge bg-light text-success" v-if="!item.selected">
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
      </div>
      <!--/Vista Bodegas-->
      <!--Vista Grupos-->
      <div class="row" v-if="showSection.groups">
        <div class="col-8">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title text-info">
                <i class="fa-solid fa-users"></i>
                Grupos Seleccionados
              </h5>
            </div>
            <div class="card-body">
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
                  <tr v-for="team in teamsTaking" :key="team">
                    <td class="text-center">
                      {{ team.group_number }}
                      <span class="badge bg-light text-secondary">
                        # {{ team.id_team }}
                      </span>
                    </td>
                    <td>{{ team.manager.first_name }} {{ team.manager.last_name }}</td>
                    <td>{{ team.warenhouse_assistant }}</td>
                    <td class="text-center">
                        {{ syncsTeams(team.id_team, 'times') }}
                    </td>
                    <td class="text-end">
                      <span>
                        {{ syncsTeams(team.id_team, 'last') }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
              <button class="btn btn-sm btn-outline-dark mt-2" @click="showDetail">
                <i class="fas fa-xmark"></i> Cerrar
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
                      <tr v-for="(user,idx) in filteredUsers" :key="user.id" @click="user.selected = !user.selected">
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
import axios from 'axios';

export default {
  name: 'NavBar',
  emits: ['updateGroups'],
  data() {
    return {
        showSection: {
          enterprises: false,
          warenhouses: false,
          groups: false,
        },
      my_query:null,
      filteredUsers: [],
    }
  },
  props: {
    reportTaking: {
      type: Object,
      required: true
    }, allWarenhouses: {
      type: Array,
      required: true
    }, confData: {
      type: Object,
      required: true
    },taking: {
      type: Object,
      required: true
    },userManager: {
      type: Object,
      required: true
    },allUsersAssistants: {
      type: Array,
      required: true
    },allEnterprises: {
      type: Array,
      required: true
    },teamsTaking:{
      type: Array,
      required: true
    },syncs:{
      type: Object,
      required: true
    }
  }
  ,computed: {
    // items completos
    full() {
      return this.reportTaking.filter(
        item => item.is_complete == true
      ).length;
    }, left_over() {
      return this.reportTaking.filter(
        item => item.is_complete == false
      ).length;
    }, percent_progress() {
      return Math.round((this.full / this.reportTaking.length) * 100);
    },allWarenhousesSelected(){
      return this.allWarenhouses.filter(
        warenhouse => warenhouse.selected == true
    )
    },allWarenhousesUnseleted(){
      return this.allWarenhouses.filter(
        warenhouse => warenhouse.selected == false
    )
  },
  }, methods: {
    // Mostramos u ocultamos las vistas de empresas, bodegas y grupos
    showDetail(name = null) {
      // si la seccion esta abierta la cerramos
      if (this.showSection[name] == true){
        this.showSection[name] = false;
        return
      }
      // cerramos todas las secciones
      this.showSection.enterprises = false;
      this.showSection.warenhouses = false;
      this.showSection.groups = false;
      // si no se envia un nombre de seccion, no hacemos nada
      if (name === null) {
        return
      }
      // abrimos la seccion que se envia
      this.showSection[name] = true;
      return
    },
    // filtramos usuarios del cuadro
    filterUsers() {
      this.filteredUsers = this.allUsersAssistants.filter(
        user => {
          return user.first_name.toLowerCase().includes(this.my_query.toLowerCase()) ||
            user.last_name.toLowerCase().includes(this.my_query.toLowerCase())
        }
      );
    },
    // Actualizamos las bodegas
    updateWarenhouses() {
      // verificamos las bodegas seleccionadas sino hay cambio no hacemos nada
      const newWarenhouses = this.allWarenhousesSelected.map(item => item.name);
      const oldWarenhouses = JSON.parse(this.taking.warenhouses);
      if ( JSON.stringify(newWarenhouses) === JSON.stringify(oldWarenhouses)){
        alert('No hay cambios');
        return
      }
      //preparamos la variable de toma
      const headers = this.confData.headers;
      this.taking.warenhouses = JSON.stringify(this.allWarenhousesSelected.filter(item => item.selected == true).map(item => item.name));
      axios.put(
        this.confData.urlUpdateTaking,
        this.taking,
        {headers}
      ).then(
        response => {
          if (response.status === 200){
            location.reload();
          }
        }
      ).catch(
        error => {
          alert('Error al actualizar las bodegas');
          consoledir(error);
        }
      )
  },
  // agregamos los grupos
  addTeams() {
    const teams = {
      'teams': this.allUsersAssistants.filter(item => item.selected)
    } ;
    
    let xhr_team = new XMLHttpRequest();
    xhr_team.open('POST', this.confData.urlUpdateTeam );
    xhr_team.setRequestHeader('Content-Type', 'application/json');
    xhr_team.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr_team.setRequestHeader('X-CSRFToken', this.confData.headers['X-CSRFToken']);
    xhr_team.onload = ()=>{
      if(xhr_team.status === 200){
        location.reload();
      }
    }
    xhr_team.send(JSON.stringify(teams));
    xhr_team.onerror = ()=>{
      alert('Error al agregar los grupos');
    }
  }, syncsTeams(id_team, typeData){

    if (typeData === 'times'){
      return this.syncs['all'].filter(i => i.id_team_id === id_team).length
    }
    
    if (typeData === 'last'){
      const lastSync = this.syncs['groups'].filter(i => i.id_team_id === id_team)
      if (lastSync[0]){
        return new Date(lastSync[0].created).toLocaleString('es-EC')
      }
      return 'NO TIENE'
    }
  }
  },mounted(){
    this.filteredUsers = this.allUsersAssistants
  },
}
</script>
