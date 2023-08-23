<template>
  <div>
    <loader v-if="show_view.loader"></loader>
    <nav-bar
        v-if="!show_view.loader"
        :taking_name="taking_name"
        :location="location"
    >
    </nav-bar>
    <div class="container" v-if="!show_view.loader">
      <div class="row mt-1">
        <div class="col text-center">
          <div class="card bg-secondary-light">
            <div class="card-body" style="--bs-card-spacer-y: 0.01rem;">
              <h5 class="card-title">Saldos SAP al 
                  <span class="text-primary">
                    {{ sap_migration_date }}
                  </span></h5>
            </div>
          </div>
        </div>
      </div>
    </div>
    <wizard
      class="mt-3"
      v-if="!show_view.loader"
      :migration_data="migration_data"
      @updateName="updateName($event)"
      @sendData="sendData($event)"
    />
  </div>
</template>

<script>
// css
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";

// time
import { format } from 'date-fns';
import { es } from 'date-fns/locale';

// fontawesome
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";

// vue components
import NavBar from './components/NavBar.vue';
import Wizard from './components/Wizard.vue';
import Loader from "./components/Loader.vue";

// axios
import axios from "axios";

// confData
import confData from "./conf.js";

// constants
var base_url = confData.baseUrl;
var csrf_token = confData["headers"]["X-CSRFToken"];


export default {
  name: 'App',
  components: {
    NavBar,
    Wizard,
    Loader,
  },data(){
    return{
      show_view: {
        loader: true,
      },
      taking_name:'',
      location:'',
      migration_data: null,
      categories: [],
      all_users: [],
      confData: confData,
    }
  },computed:{
    sap_migration_date(){
      if (this.migration_data){
        let date = new Date(this.migration_data.sap_migration.created);
        return format(date, 'dd MMMM yyyy hh:mm:ss', {locale: es});
      }
      return '';
    }
  },mounted(){
    this.LoadInitData();
  },methods:{
   LoadInitData(){
    // Cargamos datos iniciales para la aplicacion
    const headers = this.confData.headers;
     return axios.get(this.confData.urlData, {...headers}).then((response) => {
        this.migration_data = response.data;
        this.show_view.loader = false;
      }).catch((error) => {
        alert('Error al obtener los datos del reporte' + error);
      });
   }, updateName(takingName){
    //colocamos el titulo de la pagina
    document.title = takingName.takingName;
    this.taking_name = takingName.takingName;
    this.location = takingName.location;
   }, updateWarenhousesList_uncall(warenhouse){
      // actualizamos la lista de almacenes
      console.log('warenhouse', warenhouse);
      this.migration_data.warenhouses.forEach((item)=>{
          if (item.warenhouse === warenhouse){
            item.selected = !item.selected;
          }
      });
   },sendData(taking_data){
      // enviamos los datos al servidor
      this.show_view.loader = true;
      axios.post(base_url, taking_data, { headers:{
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token,
      }}).then((response) => {
        let taking = response.data;
        // redireccionamos a la pagina de reporte
        window.location.href = base_url + '/takings/detail/' + taking.id_taking;
        this.show_view.loader = false;
      }).catch((error) => {
        alert('Error al obtener los datos del reporte' + error);
      });
   }//nextmethod
  }, // next vue properties
}
</script>

<style>

body {
    font-family: 'Roboto', sans-serif;
    background-color: #f5f5f5;
    font-size: 0.80rem;
  }
  .bg-gray {
    background-color: #f1f1f1;
  }
  .bg-gray-gradient {
    background: linear-gradient(180deg, #f5f5f5 0%, #e8e8e8 100%);
  }
  .bg-success-gradient {
    background: linear-gradient(180deg, #f1f1f1 10%, #f5f5f5 100%);
  }
  .btn-secondary {
    background-color: #9b9b9b;
  }
  .navbar-brand{
    font-size: 0.90rem !important;
  }
  h5, .h5 {
    font-size: 0.90rem !important;
  }
  .progress {
  --bs-progress-height: 0.11rem;
}
.btn-sm {
  padding: 0.10rem !important;
  font-size: 0.75rem !important;
}

.table {
  border-collapse: collapse;
}


/* Eliminar el padding en las celdas */
.table td,
.table th {
  padding: 0;
}

/* Eliminar el margin en la tabla */
.table {
  margin: 0;
}

.bg-secondary-light {
  background-color: #e9ecef !important;
}
.border-blue{
  border: 1px solid #396ff9 !important;
}
</style>
