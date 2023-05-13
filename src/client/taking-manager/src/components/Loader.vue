<template>
    <div class="container mt-5">
        <div class="row">
            <div class="col text-center">
            <div class="spinner-border text-primary" style="width: 20rem; height: 20rem;" role="status">
            </div>
        </div>
        </div>
        <div class="row mt-5">
            <div class="col text-center">
                    <h1 class="text-secondary text-blink">
                        Cargando Datos...
                    </h1>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Loader'
}
</script>

<style scoped>
    @keyframes blinker {
        50% {
            opacity: 20%;
            color:red;
        }

    }
    .text-blink{
        animation: blinker 1s linear infinite;
    }
</style>