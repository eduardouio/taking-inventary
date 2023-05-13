<template>
  <div class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">TOMA #109</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <span class="nav-link">

                Inicio
              </span>
            </li>
            <li class="nav-item">
              <span class="badge rounded-pill bg-info text-dark">
                {{
                report.warenhouses | length }}</span>
            </li>
            <li class="nav-item">
              <span class="nav-link" href="#">Empresas<span class="badge rounded-pill bg-info text-dark">{{
                report.enterprises | length }}</span></span>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Bodegas <span class="badge rounded-pill bg-info text-dark">3</span></a>
            </li>
          </ul>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Pendientes:
                </span>
                <strong class="badge bg-light text-dark">12</strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Faltantes:
                </span><strong class="badge bg-warning"> 12</strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Sobrantes:
                </span><strong class="badge bg-danger"> 12</strong></span>
            </li>
            <li class="nav-item border rounded bg-secondary">
              <span class="nav-link"><span class="text-white">
                  Completos:
                </span><strong class="badge bg-success"> 12</strong></span>
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
      type: Array,
      required: true
    }
  },
}
</script>

<style></style>