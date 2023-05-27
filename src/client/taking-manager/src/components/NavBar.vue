<template>
  <div class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">TOMA # <span v-if="report.report" v-text="report.report.taking.pk"></span></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <a href="/" class="nav-link">
                  Inicio
                </a>
            </li>
            <li class="nav-item">
              <span class="nav-link">Empresas &nbsp;<span class="badge rounded-pill bg-info text-dark"> {{ total_enterprises  }}</span></span>
            </li>
            <li class="nav-item">
              <a class="nav-link">Bodegas &nbsp;<span class="badge rounded-pill bg-info text-dark"> {{total_warenhouses}}</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link">Usuarios &nbsp;<span class="badge rounded-pill bg-info text-dark"> {{total_users}}</span></a>
            </li>
          </ul>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Pendientes:
                </span>
                <strong class="badge bg-light text-dark">{{ left_over }}</strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Faltantes:
                </span><strong class="badge bg-warning"> {{missing}}</strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Sobrantes:
                </span><strong class="badge bg-danger"> {{ earrings}} </strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Completos:
                </span><strong class="badge bg-success"> {{ full }} </strong></span>
            </li>
          </ul>
          <span class="nav-div">&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <i class="fas fa-user text-secondary"></i>
              &nbsp;
              <span class="navbar-text">
                ISAAC MALAN
                &nbsp;
                <i class="fas fa-power-off text-danger"></i>
              </span>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  name: 'NavBar',
  props: {
    report: {
      type: Object,
      required: true
    }
  },computed:{
    total_enterprises(){
      return 0;
    },total_warenhouses(){ 
      return 0;
    },total_users(){
      return 0;
    },
    full(){
      return 0;
    },left_over(){
      return 0;
    },missing(){
      return 0;
    },earrings(){
      return 0;
    },
  },
}
</script>

<style></style>