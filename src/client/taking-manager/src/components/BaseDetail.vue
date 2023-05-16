<template>
    <div class="container-fluid mt-3 border p-3 bg-white">
        <div class="row bg  bg-ligth bg-gradient">
            <div class="col-1">
                <span class="badge bg-dark">
                    {{ selected_item.product.fields.type_product }}
                </span>
            </div>
            <div class="col-10 text-center">
                <h4 class="text-primary" id="app-product-desc">
                    {{ selected_item.product.fields.name }}
                    <br>
                    <small>{{ selected_item.product.fields.ean_13_code }}</small>
                </h4>
            </div>
            <div class="col text-end">
                <button class="btn btn-outline-danger fs-3" @click="showReport">
                    <i class="fas fa-close"></i>
                </button>
            </div>
        </div>
        <div class="row bg-ligth">
            <div class="col-3">
                <img :src="image_url" class="img-thumbnail">
                <div class="row">
                    <div class="col">
                        <ul class="list-group">
                            <li class="list-group-item">
                                <strong>Cod Barras:</strong>&nbsp;{{ selected_item.product.fields.ean_13_code }}
                            </li>
                            <li class="list-group-item">
                                <strong>Cod Contable:</strong>&nbsp;{{ selected_item.product.fields.account_code }}
                            </li>
                            <li class="list-group-item">
                                <strong>Cap:</strong>&nbsp;{{ selected_item.product.fields.capacity }}
                                <span class="text-seondary">&nbsp;| &nbsp;</span>
                                <strong>CxCaja:</strong>&nbsp;{{ selected_item.product.fields.quantity_per_box }}
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="d-flex align-items-start">
                    <div class="nav flex-column nav-pills me-3" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                        <button class="btn btn-white active" id="v-pills-home-tab" data-bs-toggle="pill"
                            data-bs-target="#v-pills-home" role="tab" aria-controls="v-pills-home" aria-selected="true"> <i
                                class="fas fa-clipboard-check"></i>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TOMA&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</button>
                        <button class="btn btn-white" id="v-pills-profile-tab" data-bs-toggle="pill"
                            data-bs-target="#v-pills-profile" role="tab" aria-controls="v-pills-profile"
                            aria-selected="false"> <i class="fas fa-warning"></i> &nbsp;NOVEDADES</button>
                        <button class="btn btn-white" id="v-pills-messages-tab" data-bs-toggle="pill"
                            data-bs-target="#v-pills-messages" role="tab" aria-controls="v-pills-messages"
                            aria-selected="false"><i class="fas fa-warehouse"></i>&nbsp;EXISTENCIAS</button>
                        <button class="btn btn-warning mt-5" id="recount-item"
                                href="/recounts/make/taking/121/product/02045932711101010750">
                                <i class="fas fa-share"></i> Reconteo Item
                        </button>
                    </div>
                    <div class="tab-content" id="v-pills-tabContent">
                        <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">
                            <div class="row">
                                <div class="col">
                                <table class="table table-bordered" style="widows: 100%;">
                                    <thead>
                                        <tr>
                                            <th scope="col">Grupo</th>
                                            <th scope="col">Cantidad</th>
                                            <th scope="col">Diferencia</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>Grupo 1</td>
                                                <td>10</td>
                                                <td>0</td>
                                            </tr>
                                        </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="v-pills-profile" role="tabpanel"
                            aria-labelledby="v-pills-profile-tab">...</div>
                        <div class="tab-pane fade" id="v-pills-messages" role="tabpanel"
                            aria-labelledby="v-pills-messages-tab">...</div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    //Mostamos la informacion adicional usando una tabla maestro detalle en la que se muestra la informacion de los grupos y los productos que se han tomado
    name: 'BaseDetail',
    emits: ['showReport'],
    props: {
        selected_item: {
            type: Object,
            required: true,
        },
        show_view_report: {
            type: Boolean,
            required: true,
        },
        base_url: {
            type: String,
            required: true,
        },
    }, methods: {
        showReport() {
            this.$emit('showReport');
        },
    },
    computed: {
        // si el item no tiene imagen mostramos imagen por defecto
        image_url() {
            if (this.selected_item.product.fields.image_front) {
                return this.base_url + '/media/' + this.selected_item.product.fields.image_front;
            } else {
                return this.base_url + '/static/img/generic_product.png';
            }
        },
    }
}
</script>

<style scoped></style>