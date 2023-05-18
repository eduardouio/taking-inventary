<template>
  <div>
    <loader v-if="!report"></loader>
    <nav-bar v-if="report" :report="report"></nav-bar>
    <info-bar v-if="report" :report="report"></info-bar>
    <taking-report 
      v-if="report"
      :report="report"
      :base_url="base_url"
      ></taking-report>
  </div>
</template>


<script>  
const base_url = 'http://localhost:8000';
const url_data = '/takings/api/taking-manager/88/';

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
      report: null,
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
          this.report = JSON.parse(xhr.responseText) ;
        }
      };
      xhr.send();
    }
  },
  mounted(){
    this.updateData();
  },
}
</script>

<style>
  body {
    background-color: #f5f5f5;
  }
  .bg-gray {
    background-color: #e8e8e8;
  }
  .bg-gray-gradient {
    background: linear-gradient(180deg, #f5f5f5 0%, #e8e8e8 100%);
  }
</style>
