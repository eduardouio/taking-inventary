<template>
  <div>
    <loader 
      v-if="!report"
    ></loader>
    <nav-bar
        v-if="report" 
        :report="report"
        :warenhouses="warenhouses"
        :userdata="userdata"
        :base_url="base_url"
        @updateWarenhouses="$event => updateWarenhouses($event)"
        ></nav-bar>
    <info-bar 
        v-if="report"
        :report="report"
        :show_all_takings="show_all_takings"
        :taking_is_open:="taking_is_open"
        @showAllTakings="$event => showAllTakings($event)"
        @makeRecount="$event => makeRecount($event)"
        @closeTaking="$event => closeTaking($event)"
        >
    </info-bar>
    <taking-report 
      v-if="report && filtered"
      :report="report"
      :table_takings="table_takings"
      :base_url="base_url"
      :show_all_takings="show_all_takings"
      :taking_is_open="taking_is_open"
      @makeRecount="$event => makeRecount($event)"
      ></taking-report>
  </div>
</template>


<script>  
const base_url = '';
const url_data = 'url_de_toma_item';

const userdata = {
  "username": "Datos",
  "id": 2,
  "first_name": "Eduardo",
  "last_name": "Villota",
  "email": "eduardouio7@gmail.com",
};

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";

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
      base_url: base_url,
      url_data: url_data,
      userdata: userdata,
      report: null,
      warenhouses: null,
      table_takings:null,
      show_all_takings:true,
      filtered:true,
      taking_is_open:false,
    }
  },methods: {
    // Cargamos los datos iniciales para la interfase
    updateData: function() {
      const xhr = new XMLHttpRequest();
      xhr.open("GET", this.base_url + this.url_data);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      xhr.onload = () =>{
        if (xhr.status === 200){
          // cargamos el reporte
          this.report = JSON.parse(xhr.responseText);
          // marcamos el estatus de la toma
          this.taking_is_open = this.report.taking.is_active;
          // cargamos las bodegas
          let my_warenhouses = JSON.parse(this.report.taking.warenhouses);
          this.warenhouses = my_warenhouses.map(item => {
            return {
              'name': item,
              'selected': true,
            }
            });
      // ordenamos las bodegas
      this.report.all_warenhouses.sort((a, b) => {
        if (a.name > b.name) {
          return 1;
        }
        if (a.name < b.name) {
          return -1;
        }
        return 0;
      });
      // creamos una copia del reporte
      this.table_takings = JSON.parse(xhr.responseText).report;
      // mostramos solo diferencias
      this.show_all_takings = false;
      };
    };
    xhr.onerror = () => {
      alert('Error al cargar los datos');
    };
    xhr.send();
    },
    // Actualizamos las bodegas
    updateWarenhouses: function() {
      const selected_warenhouses = this.warenhouses.filter(
        item => item.selected
      ).map(item => item.name).concat(
      this.report.all_warenhouses.filter(
          item => item.selected
        ).map(item => item.name)
      );
      
      // si no hay bodegas seleccionadas no hacemos nada
      if (selected_warenhouses.length === 0){
          return;
      }
      // actualizamos la toma
      const update_taking = this.report.taking;
      update_taking.warenhouses = JSON.stringify(selected_warenhouses);
      const xhr_taking = new XMLHttpRequest();
      xhr_taking.open(
        "PUT", 
        this.base_url + '/api/takings/update-taking/' + update_taking.id_taking + '/'
        );
      xhr_taking.setRequestHeader('Content-Type', 'application/json');
      xhr_taking.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      xhr_taking.onload = () =>{
        if (xhr_taking.status === 200){
          // cargamos el reporte
          location.reload();
          }
        }
      xhr_taking.onerror = () => {
        alert('Error al cargar los datos');
      };
      xhr_taking.send(JSON.stringify(update_taking));
      },showAllTakings() {
        this.show_all_takings = !this.show_all_takings;
      },
      // filtamos el reporte
      filterReport(){
        this.filtered = false;
        setTimeout(() => {
        this.table_takings = [];
        const report = this.report.report.map(item => item);
        if (this.show_all_takings) {
          this.table_takings = report;
          this.filtered = true;
          return;
        }
        this.table_takings = report.filter(
          item => item.is_complete === false
        );
        this.filtered = true;
        return;  
        }, 100);
      }, makeRecount(account_code){
        // check if recount all taking or one item
        let id_taking = this.report.taking.id_taking;
        let url = `/api/common/recount/${id_taking}/${account_code}/`;
        const xhr_recount = new XMLHttpRequest();
        xhr_recount.open(
          "GET", 
          this.base_url + url
          );
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
               // update item in table
          this.report.report.forEach(item => {
            if (item.product.account_code === account_code) {
              item.tk_botles = 0;
              item.tk_boxes = 0;
              item.tk_quantity = 0;
            }
          });
            }
          }
        xhr_recount.onerror = () => {
          alert('Error al actualizar el estado de la toma');
        };
        xhr_recount.send();
      }, closeTaking(id_taking){
        // set is_closed to true in taking
        let update_taking = this.report.taking;
        update_taking.is_active = false;
        const xhr_taking = new XMLHttpRequest();
        xhr_taking.open(
          "PUT", 
          this.base_url + '/api/takings/update-taking/' + id_taking + '/'
          );
        xhr_taking.setRequestHeader('Content-Type', 'application/json');
        xhr_taking.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr_taking.onload = () =>{
          if (xhr_taking.status === 200){
            // cargamos el reporte
            location.reload();
            }
          }
        xhr_taking.onerror = () => {
          alert('Error al completar la petición, toma no cerrada');
        };
        xhr_taking.send(
          JSON.stringify(update_taking)
          );
      },// next method
    },
  mounted(){
    this.updateData();
  },watch:{
    show_all_takings: function() {
      this.filterReport();
  }
  }}
</script>

<style>
  body {
    background-color: #f5f5f5;
    font-size: 0.85rem;
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
</style>
