<template>
  <div class="app">
    <DashboardPage v-if="false"/> 
    <AuditPage v-if="true"/>
  </div>
</template>

<script>


import DashboardPage from './pages/DashboardPage.vue'
import AuditPage from './pages/AuditPage.vue'

export default {
  name: 'App',
  components: {
    DashboardPage,
    AuditPage,
  }
}
</script>

<style>
</style>
