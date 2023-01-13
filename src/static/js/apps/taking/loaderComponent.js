app.component('loader', {
    template : /* vue-html */ `
        <div class="loader" v-if="!server_status.response">
        <div class="row">
            <div class="col text-center">
                <img :src="server_status.img_loader" alt="status" class="img-fluid">
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <strong class="text-info">CARGANDO...</strong>
            </div>
        </div>
        <div class="row">
            <div class="col text-center" v-if="server_status.type">
                <img :src="server_status.type === 'error' ? server_status.img_error : server_status.img_ok" alt="status" class="img-fluid">
                <strong :class="server_status.class" v-text="server_status.message"></strong>
            </div>
        </div>
    </div>
    `,
    props:['server_status'],
    data() { return {

    };
    },
})