<template>
  <div class="container-fluid mt-1 bg-light">
      <div class="row">
    <div class="progress">
    <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
    AVANCE DE TOMA
  </div>
      </div>
    <div class="row border bg-gardient-secondary rounded bg-gradient-light" style="padding: 5px;">
      <div class="col-8">
        2 de mayo de 2023
        &nbsp;| &nbsp;
        Estado:
        <i class="fas fa-play text-success"></i>&nbsp;
        <span class="text-success">Conteo Abierto, Recibiendo Datos </span>
        &nbsp;| &nbsp;
        <button class="btn btn-outline-warning btn-sm">
          <i class="fas fa-share"></i>
          Reconteo
        </button>
        &nbsp;
        <button class="btn btn-outline-danger btn-sm">
          <i class="fas fa-stop"></i>
          Detener
        </button>
      </div>
      <div class="col text-end">
        <strong class="text-info h6">
          CICLICO 02/05/2023
        </strong>
        &nbsp;
        <label class="badge bg-info">10%</label>
        &nbsp;
        <button class="btn btn-sm btn-outline-success">
          <i class="fas fa-file-excel text-success"></i>
          Reporte
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'InfoBar',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.progress {
    --bs-progress-height: 0.3rem;
}
</style>
