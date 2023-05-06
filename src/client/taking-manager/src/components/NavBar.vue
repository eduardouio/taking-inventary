<template>
    <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">TOMA #109</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Inicio</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Grupos <span class="badge rounded-pill bg-info text-dark">8</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Empresas<span class="badge rounded-pill bg-info text-dark">3</span></a>
            </li>
            <li class="nav-item">
                  <a class="nav-link" href="#">Bodegas <span class="badge rounded-pill bg-info text-dark">3</span></a>
            </li>
          </ul>
          <span class="navbar-text">
            ISAAC MALAN
            &nbsp;
            <i class="fas fa-power-off text-danger"></i>
          </span>
        </div>
      </div>
    </nav>       
    </div>    
</template>

<script>
export default {
    name: 'NavBar'
}
</script>

<style>

</style>