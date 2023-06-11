<template>
  <div>
    <nav-bar></nav-bar>
    <wizard></wizard>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";

import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";

import NavBar from './components/NavBar.vue'
import Wizard from './components/Wizard.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    Wizard,
  },data(){
    return{
      taking_name: '',
    }
  },
}
</script>

<style>

</style>
