<template>
    <div>
    <loader v-if="!item_report"></loader>
    <div class="container-fluid mt-3 border bg-white" v-if="item_report">
        <div class="row bg  bg-ligth bg-gradient">
            <div class="col-1">
                <span class="badge bg-dark">
                    {{ selected_item.product.fields.type_product }}
                </span>
            </div>
            <div class="col-10 text-center">
                <span class="text-primary" id="app-product-desc">
                    {{ selected_item.product.fields.name }}
                    <br>
                    <small>{{ selected_item.product.fields.ean_13_code }}</small>
                </span>
                <hr>
            </div>
            <div class="col text-end">
                <button class="btn btn-outline-danger fs-5" @click="showReport">
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
                                            <th>#</th>
                                            <th>Hora</th>
                                            <th scope="col">Grupo</th>
                                            <th scope="col">Cantidad</th>
                                            <th scope="col">Diferencia</th>
                                            <th><i class="fas fa-cogs"></i></th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(item, index) in item_report.query" :key="item.query">
                                                  <td class="text-center">{{ index +1 }}</td>
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
    </div>
</template>
<script>
import Loader from './Loader.vue';

export default {
  components: { Loader },
    //Mostamos la informacion adicional usando una tabla maestro detalle en la que se muestra la informacion de los grupos y los productos que se han tomado
    name: 'BaseDetail',
    componets:{
        Loader,
    },
    emits: ['showReport'],
    data(){
        return{
            item_report:null,
        }
    },
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
        report:{
            type:Object,
            required:true,
        }
    },methods: {
        showReport() {
            this.$emit('showReport');
        },
        loadDetailData(){
            console.log('obtenemos el detalle del producto');
            let url = '/takings/api/taking-detail/taking/{pk_taking}/product/{pk_product}/'.replace(
                '{pk_product}', this.selected_item.product.fields.account_code
            ).replace(
                '{pk_taking}', this.report.report.taking.pk
            )
            const xhr_data = new XMLHttpRequest();
            xhr_data.open('GET', this.base_url + url);
            xhr_data.setRequestHeader('Content-Type', 'application/json');
            xhr_data.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr_data.onload = () =>{
                this.item_report = JSON.parse(xhr_data.responseText);
            };
            xhr_data.send();

        },
    },
    mounted(){
        this.loadDetailData();
    },
    computed: {
        // si el item no tiene imagen mostramos imagen por defecto
        image_url() {
            if (this.selected_item.product.fields.image_front) {
                return this.base_url + '/media' + this.selected_item.product.fields.image_front;
            } else {
                return this.base_url + '/static/img/generic_product.png';
            }
        },
    }
}
</script>

<style scoped></style>