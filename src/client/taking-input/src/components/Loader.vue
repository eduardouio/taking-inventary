<template>
    <div>
        <div class="row">
            <div class="text-center">
            <div class="spinner-border" v-if="!server_status.response"
            style="width: 13rem; height: 13rem;" role="status" >
             <span class="visually-hidden">Cargando...</span>
             </div>
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
                    :src="server_status.issue_type === 'error' ? server_status.img_error : server_status.img_ok" 
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
            <i class="fas fa-home"></i> Recargar Aplicación
            </a>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Loader',
    emits: ['changeview'],
    props: {
        server_status: {
            type: Object,
            default: null,
            required: true,
        },
        show_view: {
            type: Object,
            default: null,
            required: true,
        },
    },methods: {
        switchView() {
           this.$emit('changeView', 'search_form');
       },
    },
    beforeUnmount() {
        this.switchView();
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