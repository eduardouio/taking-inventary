<template>
    <div class="loader" v-if="!server_status.response">
            <div class="row" v-if="server_status.type == ''">
                <div class="col text-center">
                    <img :src="server_status.img_loader" alt="status" class="img-fluid">
                </div>
            </div>
            <div class="row">
                <div class="col text-center">
                    <strong class="h2 text-info">CARGANDO...</strong>
                </div>
            </div>
            <div class="row">
                <div class="col text-center" v-if="server_status.type">
                    <img :src="server_status.type === 'error' ? server_status.img_error : server_status.img_ok" alt="status" class="img-fluid">
                    <br/>
                    <strong class="h2" :class="server_status.class" v-text="server_status.message"></strong>
                </div>
            </div>
            <a class="btn btn-secondary btn-block" v-if="!server_status.have_error_message" href="/mobile/dashboard/"><i class="fas fa-home"></i> Volver al inicio </a>
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
        }
    },
}
</script>