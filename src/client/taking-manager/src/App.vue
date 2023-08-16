<template>
  <div>
    <loader 
      v-if="!serverStatus.haveData" 
      :serverStatus="serverStatus"
    ></loader>
    <nav-bar
        v-if="serverStatus.haveData" 
        :reportTaking="reportTaking"
        :allWarenhouses="allWarenhouses"
        :allEnterprises="allEnterprises"
        :confData="confData"
        :taking="taking"
        :userManager="userManager"
        :allUsersAssistants="allUsersAssistants"
        :teamsTaking="teamsTaking"
        :syncs="syncs"
        @updateWarenhouses="$event => updateWarenhouses($event)"
        ></nav-bar>
        <info-bar 
        v-if="serverStatus.haveData" 
        :reportTaking="reportTaking"
        :isShowAllTakings="isShowAllTakings"
        :confData="confData"
        :syncs="syncs"
        :taking="taking"
        :recounts="recounts"
        @showAllTakings="$event => showAllTakings($event)"
        @makeRecount="$event => makeRecount($event)"
        @closeTaking="$event => closeTaking($event)"
        >
      </info-bar>
      <taking-report 
      v-if="serverStatus.haveData && filtered"
      :tableTakings="tableTakings"
      :reportTaking="reportTaking"
      :confData="confData"
      :isShowAllTakings="isShowAllTakings"
      :IsTakingOpen="taking.is_active"
      :serverStatus="serverStatus"
      :taking="taking"
      @makeRecount="$event => makeRecount($event)"
      ></taking-report>
  </div>
</template>
<script>  

// importamos las configuraciones
import confData from "./conf";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";

import axios from 'axios';
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";

import Loader from './components/Loader.vue';
import NavBar from "./components/NavBar.vue"
import InfoBar from "./components/InfoBar.vue"
import TakingReport from "./components/TakingReport.vue"
import GroupsInfo from './components/GroupsInfo.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    InfoBar,
    TakingReport,
    GroupsInfo,
    Loader,
  },data() {
    return {
      confData: confData,
      serverStatus:{
        fetching: false,
        error: false,
        message: null,
        haveData: false,
      },
      taking: null,
      allEnterprises: null,
      reportTaking: null,
      teamsTaking: null,
      userManager: null,
      allWarenhouses: null,
      allUsersAssistants:null,
      recounts: null,
      isShowAllTakings:true,
      filtered:true,
      takingIsOpen:false,
      tableTakings: [],
    }
  },methods: {
    // Cargamos los datos iniciales para la interfase
    updateData: async function() {
      //enceramos datos iniciales
      this.taking = null;
      this.allEnterprises = null;
      this.reportTaking = null;
      this.teamsTaking = null;
      this.userManager = null;
      this.allWarenhouses = null;
      this.allUsersAssistants =null;
      this.recounts = null;
      this.syncs = null;
      // variables auxiliares
      this.tableTakings = [];
      this.isShowAllTakings = false;
      this.filtered = true;
      this.takingIsOpen = false;
      this.serverStatus.fetching = true;
      this.serverStatus.haveData = false;
      // headers
      const headers = this.confData.headers;

      // peticion inicial de datos
      axios.get(this.confData.urlData,{headers}).then(response => {
        const responseData = response.data;
        // seteamos las variables con la respuesta
        this.taking = responseData.taking;
        this.allEnterprises = responseData.enterprises;
        this.reportTaking = responseData.report;
        this.teamsTaking = responseData.teams.sort((a, b) => a.group_number - b.group_number);
        this.userManager = responseData.manager;
        this.allWarenhouses = responseData.all_warenhouses.sort((a, b) => a.name.localeCompare(b.name));
        this.allUsersAssistants = responseData.all_users_assistants;
        this.recounts = responseData.recounts;
        this.syncs = responseData.syncs;
        // variables auxiliares
        this.serverStatus.fetching = false;
        this.takingIsOpen = responseData.taking.is_active;
        this.isShowAllTakings = false;
        this.serverStatus.haveData = true;
        // filtramos el reporte
        this.filterReport();
      }).catch(e => {
        this.serverStatus.error = true;
        this.serverStatus.fetching = false;
        this.serverStatus.message = 'No es posible conectar con el servidor';
        console.dir(e);
      });      
    },showAllTakings() {
        this.isShowAllTakings = !this.isShowAllTakings;
        this.filterReport();
      },
      // filtamos el reporte
      filterReport(){
        this.filtered = false;
        setTimeout(() => {
          this.filtered = true;
          if (this.isShowAllTakings) {
          this.tableTakings = this.reportTaking.map(item => item);
          return;
        }
        this.tableTakings = this.reportTaking.filter( item => item.is_complete === false);
        return;  
        }, 50);
     
      }, makeRecount(account_code){
        this.serverStatus.fetching = true;
        this.serverStatus.haveData = false;

        let url = this.confData.urlRecount.replace('{accountCode}', account_code)
        const xhr_recount = new XMLHttpRequest();
        xhr_recount.open("GET", url);
        xhr_recount.setRequestHeader('Content-Type', 'application/json');
        xhr_recount.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr_recount.onload = () =>{
          if (xhr_recount.status === 200){
            let response = JSON.parse(xhr_recount.responseText);
            if (response.status != 'ok'){
                alert(`Error al ejecutar accion ${response.status}`);
                return;
            }
            if(account_code === 'all'){
              location.reload();
              return;
            }
            // update item in table
          this.serverStatus.fetching = false;
          this.serverStatus.haveData = true;
          this.reportTaking.forEach(item => {
            if (item.product.account_code === account_code) {
              item.tk_botles = 0;
              item.tk_boxes = 0;
              item.tk_quantity = 0;
            }
          });
            }
          }
        xhr_recount.onerror = (error) => {
          this.serverStatus.fetching = false;
          this.serverStatus.error = true;
          this.serverStatus.message = 'Error al actualizar el estado de la toma';
          console.dir(error);
        };
        xhr_recount.send();
      }, closeTaking(id_taking){
        this.serverStatus.fetching = true;
        this.serverStatus.haveData = false;
        // set is_closed to true in taking
        let update_taking = this.taking;
        update_taking.is_active = false;
        update_taking.date_end_taking = new Date().getTime();
        
        const xhr_taking = new XMLHttpRequest();
        xhr_taking.open("PUT", this.confData.urlUpdateTaking);
        xhr_taking.setRequestHeader('Content-Type', 'application/json');
        xhr_taking.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr_taking.setRequestHeader('X-CSRFToken', this.confData.headers['X-CSRFToken']);
        xhr_taking.onload = () =>{
          if (xhr_taking.status === 200){
            // cargamos el reporte
            location.reload();
            }
          }
        xhr_taking.onerror = (error) => {
          this.serverStatus.fetching = false;
          this.serverStatus.error = true;
          this.serverStatus.message = 'Error al actualizar el estado de la toma';
          console.dir(error);
        };
        xhr_taking.send(
          JSON.stringify(update_taking)
          );
      },
    },
  mounted(){
    this.updateData();
  },watch:{
    isShowAllTakings: function() {
      if(this.takingReport){
        this.filterReport();
      }
  }
  }}
</script>

<style>
  body {
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
</style>