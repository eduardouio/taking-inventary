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
                    <div class="tab-content" id="v-pills-tabContent" style="width: 100%;">
                        <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab"> 
                            <div class="bg-gray border">
                            <div class="row">
                                <div class="col">
                                    <div class="row text-center">
                                            <div class="col text-center">
                                                <span class="h3 text-secondary">Stock</span>
                                            </div>
                                            <div class="col text-center">
                                                <span class="h3 text-primary">Toma</span>
                                            </div>
                                            <div class="col text-center"><h3 :class="status_taking.class">{{ status_taking.text }}</h3></div>
                                            </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col">
                                    <div class="row text-center">
                                            <div class="col text-center">
                                                <span class="h2 text-secondary">{{ selected_item.sap_stock }}</span>
                                            </div>
                                            <div class="col text-center">
                                                <span class="h2 text-primary">{{ total_quantity }}</span>
                                            </div>
                                            <div class="col text-center"><h2 v-if="sale_boxes">{{ sale_boxes }}</h2></div>
                                            </div>
                                </div>
                            </div>
                            </div>
                            <div class="row mt-2">
                                <div class="col">
                                <table class="table table-bordered table-hover">
                                    <thead>
                                        <tr class="text-center bg-gray-gradient">
                                            <th>#</th>
                                            <th>Hora</th>
                                            <th>Grupo</th>
                                            <th>Manager</th>
                                            <th>Cajas</th>
                                            <th>Unds</th>
                                            <th>Total</th>
                                            <th class="text-center text-danger"><i class="fas fa-trash"></i></th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(item, index) in item_report.query" :key="item.query">
                                                  <td class="text-center">{{ index +1 }}</td>
                                                  <td>{{ new Date(item.detail.fields.created).toLocaleString('es-EC') }}</td>
                                                  <td class="text-center">{{ item.team.group_number }}</td>
                                                  <td> {{ item.team.manager }}</td>
                                                  <td class="text-end">{{ item.detail.fields.taking_total_boxes }}</td>
                                                  <td class="text-end">{{ item.detail.fields.taking_total_bottles }}</td>
                                                  <td class="text-end bg-gray">{{ item.detail.fields.quantity }}</td>
                                                  <td class="text-center text-danger"><i class="fas fa-minus"></i></td>
                                            </tr>
                                            <tr class="bg-success-gradient text-bold">
                                                <td colspan="4" class="text-end"><strong>Sumas:</strong></td>
                                                <td class="text-end"><strong>{{ total_boxes }}</strong></td>
                                                <td class="text-end"><strong>{{ total_bottles }}</strong></td>
                                                <td class="text-end"><strong>{{ total_quantity }}</strong></td>
                                                <td class="text-center">--</td>
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
        },total_boxes(){
            return this.item_report.query.reduce((a, b) => a + b.detail.fields.taking_total_boxes, 0)
        },total_bottles(){
            return this.item_report.query.reduce((a, b) => a + b.detail.fields.taking_total_bottles, 0)
        },total_quantity(){
            return this.item_report.query.reduce((a, b) => a + b.detail.fields.quantity, 0)
        },status_taking(){
            if(this.selected_item.sap_stock === this.total_quantity){
                return { text: 'Completo', class: 'text-success' };
            }
            if (this.selected_item.sap_stock > this.total_quantity) {
                return { text: 'Faltante', class: 'text-warning' };
            }
            if (this.selected_item.sap_stock < this.total_quantity) {
                return { text: 'Sobrante', class: 'text-danger' };
            }
        },sale_boxes(){
            return Math.abs(this.selected_item.sap_stock - this.total_quantity)
        },
        news_report(){
            return true;
        },
    },
}
</script>

<style scoped></style>