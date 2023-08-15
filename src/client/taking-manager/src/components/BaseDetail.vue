<template>
    <div>
        <loader
        v-if="!item_report"
        :serverStatus="serverStatus"
        >
    </loader>
        <div class="container-fluid mt-3 border bg-white" v-if="item_report">
            <div class="row bg  bg-ligth bg-gradient h5">
                <div class="col-1">
                    <span class="badge bg-dark">
                        {{ selected_item.product.type_product }}
                    </span>
                </div>
                <div class="col-10 text-center">
                    <span class="text-primary" id="app-product-desc">
                        {{ selected_item.product.name }}
                        &nbsp;
                        <span class="text-dark">
                            Cajas X {{ selected_item.product.quantity_per_box }} Unds
                        </span>
                        <br>
                        <small>{{ selected_item.product.ean_13_code }}</small>
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
                                <li class="list-group-item text-center" :class="status_taking.class">
                                    <i :class="status_taking.icon"></i>
                                    &nbsp;
                                    <strong>{{ status_taking.text }}</strong>
                                </li>
                                <li class="list-group-item">
                                    <strong>Cod Contable:</strong>&nbsp;{{ selected_item.product.account_code }}
                                    &nbsp;| &nbsp;
                                    <span class="badge bg-dark">
                                        #: {{ selected_item.product.id_product }}
                                    </span>
                                </li>
                                <li class="list-group-item">
                                    <strong>Cap:</strong>&nbsp;{{ selected_item.product.capacity }}
                                    <span class="text-seondary">&nbsp;| &nbsp;</span>
                                    <strong>CxCaja:</strong>&nbsp;{{ selected_item.product.quantity_per_box }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="d-flex align-items-start">
                        <div class="nav flex-column nav-pills me-3" id="v-pills-tab" role="tablist"
                            aria-orientation="vertical">
                            <button class="btn btn-white active btn-sm" data-bs-toggle="pill"
                                data-bs-target="#v-pills-home">
                                <i class="fas fa-clipboard-check"></i><br>Toma
                            </button>
                            <button class="btn btn-white btn-sm" data-bs-toggle="pill" data-bs-target="#v-pills-profile">
                                <i class="fas fa-warning"></i> &nbsp;Novedades
                            </button>
                            <button class="btn btn-white btn-sm" data-bs-toggle="pill" data-bs-target="#v-pills-messages">
                                <i class="fas fa-warehouse"></i>&nbsp;Existencias
                            </button>
                            <button class="btn btn-warning mt-5 btn-sm" id="recount-item" @click="makeRecount" v-if="taking.is_active && status_taking.text != 'Completo'">
                                <span v-if="confirm_recount" class="text-danger"><i class="fas fa-check"></i>
                                    CONFIRMAR</span>
                                <span v-else>
                                    <i class="fas fa-share"></i>
                                    RECONTEO
                                </span>
                            </button>
                        </div>
                        <div class="tab-content" id="v-pills-tabContent" style="width: 100%;">
                            <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel"
                                aria-labelledby="v-pills-home-tab">
                                <div class="border">
                                    <div class="row">
                                        <div class="col">
                                            <div class="row text-center">
                                                <div class="col text-center">
                                                    <span class="h6">Stock</span>
                                                    &nbsp;
                                                    <span class="h6">{{ selected_item.sap_stock }}</span>
                                                </div>
                                                <div class="col text-center">
                                                    <span class="text-primary h6">Toma</span>
                                                    &nbsp;
                                                    <span class="text-primary h6">{{ total_quantity }}</span>
                                                </div>
                                                <div class="col text-center" :class="status_taking.class">
                                                    <i class="" :class="status_taking.icon"></i>
                                                    &nbsp;
                                                    <span class="h6">{{ status_taking.text }}</span>
                                                    &nbsp;
                                                    <span class="h6" v-if="sale_boxes">{{ sale_boxes }}</span>
                                                </div>
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
                                                <tr v-for="(item, index) in item_report.takings" :key="item">
                                                    <td class="text-center">{{ index + 1 }}</td>
                                                    <td>{{ new Date(item.taking.created).toLocaleString('es-EC') }}
                                                    </td>
                                                    <td class="text-center">{{ item.team.group_number }} </td>
                                                    <td>{{ item.user.first_name }} {{ item.user.last_name }}</td>
                                                    <td class="text-end">{{ item.taking.taking_total_boxes }}</td>
                                                    <td class="text-end">{{ item.taking.taking_total_bottles }}</td>
                                                    <td class="text-end bg-gray">{{ item.taking.quantity }}</td>
                                                    <td class="text-center text-danger" @click="delteItemDetail(item.taking.id_taking_detail)">
                                                        <span v-if="taking.is_active">
                                                            <i class="fas fa-minus" v-if="!confirm_delete_detail"></i>
                                                            <i class="fa-solid fa-check text-danger" v-else></i>
                                                        </span>
                                                        <span v-else>
                                                            --
                                                        </span>
                                                    </td>
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
                                aria-labelledby="v-pills-profile-tab">
                                <div class="row mt-2">
                                    <div class="col">
                                        <table class="table table-bordered table-hover">
                                            <thead>
                                                <tr class="text-center bg-gray-gradient">
                                                    <th>#</th>
                                                    <th>Grupo</th>
                                                    <th>Novedad</th>
                                                    <th>Año</th>
                                                    <th>Caducidad</th>
                                                    <th>Unds</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="(item, index) in item_report.takings" :key="item">
                                                    <td>{{ index + 1 }}</td>
                                                    <td><span class="badge bg-info">G#{{ item.team.group_number }}</span>
                                                        {{ item.user.first_name }} {{ item.user.last_name }}</td>
                                                    <td>
                                                        {{ item.taking.notes ? item.taking.notes : '--' }}
                                                    </td>
                                                    <td class="text-end">{{ item.taking.year ? item.taking.year : '--' }}
                                                    </td>
                                                    <td class="text-end">
                                                        {{ item.taking.date_expiry ? new
                                                            Date(item.taking.date_expiry).toLocaleDateString('es-EC') : '--' }}
                                                    </td>
                                                    <td class="text-end">{{ item.taking.quantity }}</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="v-pills-messages" role="tabpanel"
                                aria-labelledby="v-pills-messages-tab">
                                <div class="row">
                                    <div class="col">
                                        <table class="table table-bordered table-hover">
                                            <thead>
                                                <tr class="text-center bg-gray-gradient">
                                                    <th>#</th>
                                                    <th>Empresa</th>
                                                    <th>Bodega</th>
                                                    <th>Cajas</th>
                                                    <th>Unds</th>
                                                    <th>Total</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="(item, index) in item_report.migrations" :key="item">
                                                    <td>{{ index + 1 }}</td>
                                                    <td>{{ item.company_name }}</td>
                                                    <td><span class="badge bg-success">{{ item.id_warenhouse_sap_code
                                                    }}</span> {{ item.warenhouse_name }} </td>
                                                    <td class="text-end">{{ Math.floor(item.on_hand /
                                                        selected_item.product.quantity_per_box) }}</td>
                                                    <td class="text-end">{{ item.on_hand - Math.floor(item.on_hand /
                                                        selected_item.product.quantity_per_box) *
                                                        selected_item.product.quantity_per_box }}</td>
                                                    <td class="text-end">{{ item.on_hand }}</td>
                                                </tr>
                                                <tr class="bg-gray-gradient">
                                                    <th colspan="3">Sumas</th>
                                                    <td class="text-end"><strong>{{ Math.floor(total_stocks /
                                                        selected_item.product.quantity_per_box) }}</strong></td>
                                                    <td class="text-end"><strong>{{ total_stocks - Math.floor(total_stocks /
                                                        selected_item.product.quantity_per_box) *
                                                        selected_item.product.quantity_per_box }}</strong></td>
                                                    <td class="text-end"><strong>{{ total_stocks }}</strong></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>
import confData from '../conf';
import Loader from './Loader.vue';

export default {
    components: { Loader },
    //Mostamos la informacion adicional usando una tabla maestro detalle en l
    // a que se muestra la informacion de los grupos y los productos que se han tomado
    name: 'BaseDetail',
    componets: {
        Loader,
    },
    emits: ['showReport', 'makeRecount',],
    data() {
        return {
            item_report: null,
            stock_report: null,
            confirm_recount: false,
            confirm_delete_detail: false,
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
        confData: {
            type: Object,
            required: true,
        },
        reportTaking: {
            type: Object,
            required: true,
        }, taking: {
            type: Object,
            required: true,
        },serverStatus:{
            type:Object,
            required:true
        }
    }, methods: {
        showReport() {
            this.$emit('showReport');
        }, sendGetRequest(url, callback) {
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.onload = () => {
                if (xhr.status === 200) {
                    return callback(JSON.parse(xhr.responseText));
                }
                alert('Error en peticion GET');
            };
            xhr.onerror = () => {
                alert('Error en peticion GET evento on onerror');
            };
            xhr.send();
        }, loadTakingData(item_report) {
            this.item_report = item_report;
        }, makeRecount() { // realiza el reconteo del item
            // validamos que se haya confirmado el reconteo, si no se valida se pasa a true
            if (!this.confirm_recount) {
                this.confirm_recount = true;
                return false;
            }
            // realizamos el emit al padre para que se genere el reconteo
            this.$emit(
                'makeRecount', this.selected_item.product.account_code
                );
            this.showReport();
            // setamos le contador nuevamente a false
            this.confirm_recount = false;
        }, delteItemDetail(id_taking_detail){
            if (!this.taking.is_active){
                return
            }

            if (!this.confirm_delete_detail){
                this.confirm_delete_detail = true;
                return;
            }

            let url = confData.urlDeleteTaking.replace(
                        '{idTakingDetail}', id_taking_detail
            );
            let xhr_item_detail = new XMLHttpRequest();
            xhr_item_detail.open('DELETE',url);

            xhr_item_detail.setRequestHeader('Content-Type', 'application/json');
            xhr_item_detail.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr_item_detail.setRequestHeader('X-CSRFToken', confData.headers['X-CSRFToken']);
        
            xhr_item_detail.onload = () => {
                if (xhr_item_detail.status === 204) {
                    this.item_report.takings = this.item_report.takings.filter(
                        item => { return item.taking.id_taking_detail !== id_taking_detail }
                    );
                    location.reload();

                } else {
                    alert('Error en peticion DELETE');
                }
            };

            xhr_item_detail.onerror = () => {
                alert('Error en peticion DELETE evento on onerror');
            };
            xhr_item_detail.send();
        },//next method
    },
    mounted() {
        // cargamos informacion de stock y toma del producto
        let url = this.confData.urlTakingProduct.replace(
            '{accountCode}', this.selected_item.product.account_code
        );
        this.sendGetRequest(url,this.loadTakingData);
    }, unmounted() {
        // enceramos los reportes
        this.item_report = null;
    },
    computed: {
        // si el item no tiene imagen mostramos imagen por defecto
        image_url() {
            if (this.selected_item.product.image_front) {
                return this.confData.baseUrl + this.selected_item.product.image_front;
            } else {
                return this.confData.baseUrl + '/static/img/generic_product.png';
            }
        }, total_boxes() {
            return this.item_report.takings.reduce((a, b) => a + b.taking.taking_total_boxes, 0)
        }, total_bottles() {
            return this.item_report.takings.reduce((a, b) => a + b.taking.taking_total_bottles, 0)
        }, total_quantity() {
            return this.item_report.takings.reduce((a, b) => a + b.taking.quantity, 0)
        }, status_taking() {
            if (this.selected_item.sap_stock === this.total_quantity) {
                return { text: 'Completo', class: 'text-success', icon: 'fas fa-check' };
            }
            if (this.selected_item.sap_stock > this.total_quantity) {
                return { text: 'Faltante', class: 'text-warning', icon: 'fas fa-exclamation-triangle' };
            }
            if (this.selected_item.sap_stock < this.total_quantity) {
                return { text: 'Sobrante', class: 'text-danger', icon: 'fas fa-exclamation-triangle' };
            }
        }, sale_boxes() {
            return Math.abs(this.selected_item.sap_stock - this.total_quantity)
        }, total_stocks() {
            return this.item_report.migrations.reduce((a, b) => a + b.on_hand, 0)
        }, boxesConverter(units) {
            if (typeof (units) != "number") {
                return {
                    boxes: 0, bottles: 0
                };
            }

            let boxes = Math.floor(units / this.selected_item.product.quantity_per_box);
            let bottles = units % this.selected_item.product.quantity_per_box;
            return {
                boxes: boxes, bottles: bottles
            };
        },
    },
}
</script>