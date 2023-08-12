<template>
    <div class="container mt-5">
        <div class="row" v-if="serverStatus.fetching">
            <div class="col text-center">
            <div class="spinner-border text-primary" style="width: 20rem; height: 20rem;" role="status">
            </div>
        </div>
        </div>
        <div class="row mt-5" v-if="!serverStatus.error">
            <div class="col text-center">
                    <h1 class="text-secondary text-blink">
                        Cargando Datos...
                    </h1>
            </div>
        </div>
        <div class="row mt-5 p-5" v-if="serverStatus.error">
            <div class="col text-center">
                    <h1 class="text-danger">
                        {{ serverStatus.message  }}
                    </h1>
            </div>
    </div>
</div>
</template>
<script>
export default {
    name: 'Loader',
    props: {
        serverStatus: {
            type: Object,
            required: true,
        },
    },
}
</script>

<style scoped>
    @keyframes blinker {
        50% {
            opacity: 40%;
            color:red;
        }

    }
    .text-blink{
        animation: blinker 1s linear infinite;
    }
</style>