<template>
  <div>
    <loader v-if="show_view.loader"></loader>
    <nav-bar
        v-if="!show_view.loader"
        :taking_name="taking_name"
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

// constants
var base_url = '';
var url_data = '/api/common/wizard-assistant/1/';
var csrf_token = 'colocar_el_token_aqui';


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
      migration_data: null,
      categories: [],
      all_users: [],
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
     return axios.get(base_url + url_data, {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      }).then((response) => {
        this.migration_data = response.data;
        this.show_view.loader = false;
      }).catch((error) => {
        alert('Error al obtener los datos del reporte' + error);
      });
   }, updateName(title){
    //colocamos el titulo de la pagina
    document.title = title;
    this.taking_name = title;
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
  font-size: 14px;
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
