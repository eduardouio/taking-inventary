<template>
  <div class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Asistente <small class="text-primary">{{ taking_name }} </small></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a href="/" class="nav-link">
                <i class="fa-solid fa-home"></i>
                Inicio
              </a>
            </li>
            <li class="nav-item">
              <a href="/sap/" class="nav-link">
                <i class="fa-solid fa-server"></i>
                Saldos SAP
              </a>
            </li>
            <li class="nav-item">
              <a href="/takings/" class="nav-link">
                <i class="fa-solid fa-list-check"></i>
                Tomas
              </a>
            </li>
            <li>
              &nbsp;
            </li>
          </ul>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item border">
              <span class="nav-link"><span>
                  Bodegas:
                </span>
                <strong class="badge rounded-pill bg-light text-dark">12</strong>
              </span>
            </li>
            &nbsp;
            <li class="nav-item border">
              <span class="nav-link"><span>
                  Grupos:
                </span>
                <strong class="badge rounded-pill bg-light text-dark">1</strong>
              </span>
            </li>
          </ul>
          <span class="nav-div">&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item text-primary">
              <i class="fas fa-user text-secondary"></i>
              &nbsp;
              Eduardo Villota
              &nbsp;
              <span class="navbar-text">
                &nbsp;
                <a href="/accounts/logout/">
                  <i class="fas fa-power-off text-danger"></i>
                </a>
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
  emits: [],
  data() {
    return {
      name: 'NavBar',
    }
  },
  props: {
    taking_name: {
      type: String,
      default: ''
    }
  }, methods: {
    // Mostramos 
  }
}
</script>
<style>
</style>