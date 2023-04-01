<template>
    <div>
        <div class="row">
            <div class="col text-center" v-if="!server_status.response" >
                <img :src="server_status.img_loader" alt="status" class="img-fluid">
            </div>
        </div>
        <div class="row">
            <div class="col text-center blink">
                <strong class="h2 text-primary">CARGANDO APLICACIÓN...</strong>
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <img 
                    style="width: 80px"
                    :src="server_status.type === 'error' ? server_status.img_error : server_status.img_ok" 
                    alt="status"
                    class="img-fluid">
            </div>
        </div>
        <div class="row text-center">
            <strong 
                class="h5" 
                :class="server_status.issue_type === 'error' ? 'text-danger' : 'text-success'"
                v-text="server_status.message">
            </strong>
        </div>
        <div class="row text-center">
            <a class="btn btn-primary btn-block" href="/mobile/dashboard/">
            <i class="fas fa-home"></i> Volver al inicio
            </a>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Loader',
    props: {
        server_status: {
            type: Object,
            default: null,
            required: true,
        },
    },
}
</script>
<style>
.blink {
    animation: blinker 4s linear infinite;
}

@keyframes blinker {
    50% {
        opacity: 0.2;
    }
    100% {
        opacity: 1;
    }
    
}
</style>