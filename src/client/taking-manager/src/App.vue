<template>
  <div>
    <nav-bar></nav-bar>
      <info-bar></info-bar>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";

import NavBar from "./components/NavBar.vue"
import InfoBar from "./components/InfoBar.vue"

export default {
  name: 'App',
  components: {
    NavBar,
    InfoBar,
  }
}
</script>

<style>
</style>
