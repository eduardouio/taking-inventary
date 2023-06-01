<template>
  <div class="container-fluid mt-1 bg-light">
    <div class="row">
      <div class="progress">
        <div class="progress-bar bg-success" role="progressbar" :style="{ 'width': percent_progress + '%' }"
          :aria-valuenow="percent_progress" aria-valuemin="0" aria-valuemax="100"></div>
        AVANCE DE TOMA
      </div>
    </div>
    <div class="row border bg-gardient-secondary rounded bg-gradient-light" style="padding: 5px;">
      <div class="col-8">
        {{ new Date(report.taking.created).toLocaleString('es-Ec') }}
        &nbsp;| &nbsp;
        Estado:
        <span v-if="report.taking.is_active">
          <i class="fas fa-play text-success"></i>&nbsp;
          <span class="text-success">Conteo Abierto, Recibiendo Datos </span>
        </span>
        <span v-else>
          <i class="fas fa-stop text-danger"></i>&nbsp;
          <span class="text-danger">Conteo Cerrado </span>
        </span>
        &nbsp;| &nbsp;
        <button class="btn btn-outline-warning btn-sm" v-if="report.taking.is_active">
          <i class="fas fa-share"></i>
          Reconteo
        </button>
        &nbsp;
        <button class="btn btn-outline-danger btn-sm" v-if="report.taking.is_active">
          <i class="fas fa-stop"></i>
          Cerrar Toma
        </button>
        &nbsp;
        <button class="btn btn-outline-secondary btn-sm" @click="showAllTakings">
          <i class="fas fa-eye"></i>
          &nbsp;
          <span v-if="show_all_takings" class="text-success">Mostrar Diferencias</span>
          <span v-else class="text-danger">Mostrar Todo</span>
        </button>
      </div>
      <div class="col text-end">
        <strong class="text-info h6">
          {{ report.taking.name }}
        </strong>
        &nbsp;
        <button class="btn btn-outline-secondary btn-sm">
          <i class="fas fa-file-excel text-success"></i>
          Reporte Diferencias
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'InfoBar',
  emits: ['showAllTakings'],
  props: {
    report: {
      type: Object,
      required: true,
    }, show_all_takings: {
      type: Boolean,
      required: true,
    }
  }, computed: {
    // items completos
    full() {
      return this.report.report.filter(
        item => item.is_complete == true
      ).length;
    }, left_over() {
      return this.report.report.filter(
        item => item.is_complete == false
      ).length;
    }, percent_progress() {
      return Math.round((this.full / this.report.report.length) * 100);
    }
  }, methods: {
    showAllTakings() {
      this.$emit('showAllTakings');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.progress {
  --bs-progress-height: 0.3rem;
}
</style>
