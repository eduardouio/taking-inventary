<template>
  <div>
    {{ reportData }}
    <nav-bar></nav-bar>
    <wizard></wizard>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";

import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";

import {mapState, mapActions} from 'vuex';


import NavBar from './components/NavBar.vue';
import Wizard from './components/Wizard.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    Wizard,
  },data(){
    return{
      taking_name: '',
    }
  },computed:{
    ...mapState(['reportData']),
  },created(){
    this.getJsonData();
  },methods:{
    takeName(){
      this.taking_name = this.$store.state.name
    }, ...mapActions(['getJsonData']),
  }
}
</script>

<style>

</style>
