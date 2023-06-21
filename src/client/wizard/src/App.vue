<template>
  <div>
    <loader v-if="show_view.loader"></loader>
    <nav-bar
        v-if="!show_view.loader"
        :taking_name="taking_name"
    >
    </nav-bar>
    <div class="container" v-if="!show_view.loader">
      <div class="row mt-3">
        <div class="col text-center">
          <div class="card">
            <div class="card-body">
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
      v-if="!show_view.loader"
      :migration_data="migration_data"
      @updateName="updateName($event)"
    ></wizard>
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
const base_url = 'http://localhost:8000';
const url_data = '/api/common/wizard-assistant/1/';


export default {
  name: 'App',
  components: {
    NavBar,
    Wizard,
    Loader,
  },data(){
    return{
      data: null,
      show_view: {
        loader: true,
      },
      taking_name:'',
      migration_data:null
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
        console.log('Respuesta del servidor');
        this.migration_data = response.data;
        this.show_view.loader = false;
      }).catch((error) => {
        alert('Error al obtener los datos del reporte' + error);
      });
   }, updateName(title){
    console.log('llamada funcion principal');
    //colocamos el titulo de la pagina
    document.title = title;
    this.taking_name = title;
   },//nextmethod
  }, // next vue properties
}
</script>

<style>

</style>
