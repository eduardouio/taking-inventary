<template>
  <div class="app">
    <JustifyPage v-if="0"/>
    <DashboardPage v-if="0"/> 
    <AuditPage v-if="1"/>
  </div>
</template>

<script>


import DashboardPage from './pages/DashboardPage.vue'
import JustifyPage from './pages/JustifyPage.vue'
import AuditPage from './pages/AuditPage.vue'

export default {
  name: 'App',
  components: {
    DashboardPage,
    JustifyPage,
    AuditPage,
  }
}
</script>

<style>
</style>
