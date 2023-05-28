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
      ></nav-bar>
    <info-bar 
        v-if="report"
        :report="report"
        :warenhouses="warenhouses"
        >
    </info-bar>
    <taking-report 
      v-if="report"
      :report="report"
      :base_url="base_url"
      ></taking-report>
  </div>
</template>


<script>  
const base_url = 'http://localhost:8000';
//const url_data = '/api/all-taking-data/118/';
const url_data = '/api/all-taking-data/1/';
const userdata = {
  "username": "Eduardo Villota",
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
          this.report = JSON.parse(xhr.responseText);
          this.warenhouses = JSON.parse(this.report.taking.warenhouses);
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
</style>
