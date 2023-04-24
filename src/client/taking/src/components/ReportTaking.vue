<template>
    <div class="card card-outline card-primary">
        <div class="card-header">
            <div v-if="report.length && show_report">
                <div class="row">
                    <div class="col text-center">
                        <i class="fas fa-table"></i>
                        <strong class="h6">
                            {{ taking.fields.name }}
                            <br>
                            Reporte Toma <small class="text-info">[{{ report.length }}] items</small>
                        </strong>
                        <br>
                        <span v-text="new Date(taking.fields.created).toLocaleString('es-EC')"></span>
                        <br>
                        <button
                            @click="downloadReport"
                            class="btn btn-primary btn-sm">
                            <i class="fas fa-file-excel"></i> Descargar
                        </button>
                    </div>
                </div>
                <div class="row mt-1">
                    <div class="col">
                        <table class="mi_table table table-striped " style="width:100%;">
                            <thead>
                                <tr class="bg-secondary">
                                    <th class="text-center">#</th>
                                    <th class="text-center">Producto</th>
                                    <th class="text-center">Cajas</th>
                                    <th class="text-center">Unds</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(item, index) in report" :key="item.pk" @click="showTaking(item)">
                                    <td class="text-center">{{ index + 1 }}</td>
                                    <td class=""> <i class="fas fa-exclamation-triangle text-warning" v-if="item.notes"></i>
                                        {{ item.product.fields.name }}</td>
                                    <td class="text-end">{{ item.taking_total_boxes }}</td>
                                    <td class="text-end">{{ item.taking_total_bottles }}</td>
                                </tr>
                                <tr class="bg-secondary">
                                    <td class="text-end" colspan="2"> <strong>TOTALES</strong></td>
                                    <td class="text-end"><strong v-text="total_boxes"></strong> </td>
                                    <td class="text-end"><strong v-text="total_bottles"></strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="row mt-3">
                    <button class="btn btn-block" :class="class_sync_btn" @click=sendReport()
                        :disabled="disable_button_send">
                        <i class="fas fa-sync"></i>
                        {{ message_button }}
                        <small>
                            [<span v-text="report.length"></span> items]
                        </small>
                    </button>
                </div>
            </div>
            <div v-if="!report.length" class="text-center">
                <strong class="text-info H2">SIN DATOS</strong>
            </div>
            <div v-if="show_taking" class="bg-white">
                <div class="card" style="width: 100%;">
                    <div class="row">
                        <div class="col text-center">
                            <img 
                            :src="selected_taking.product.fields.image_front ? selected_taking.product.fields.image_front : default_picture" 
                            class="card-img-top img-thumbnail"
                            alt="Imagen Producto"
                            style="width:12em; height:auto;"
                            >
                        </div>
                    </div>
                    <div class="card-body">
                        <h5 class="card-title text-center text-primary">{{ selected_taking.product.fields.name }}</h5>
                        <p class="card-text text-secondary">
                            <span v-if="selected_taking.notes" v-text="selected_taking.notes"></span>
                            <span v-else="" class="text-secondary">Sin Novedad</span>
                        </p>
                    </div>
                    <ul class="list-group list-group-flush fs-5 text">
                        <li class="list-group-item">
                            <div class="row">
                                <div class="col-5 text-end">
                                    <span class="text-secondary">Cajas:</span>
                                </div>
                                <div class="col text-end">
                                    <strong>
                                    {{ selected_taking.taking_total_boxes }}
                                </strong>
                                </div>
                            </div>
                        </li>
                        <li class="list-group-item">
                            <div class="row">
                                <div class="col-5 text-end">
                                    <span class="text-secondary">Unidades:</span>
                                </div>
                                <div class="col text-end">
                                    <strong>
                                    {{ selected_taking.taking_total_bottles }}
                                </strong>
                                </div>
                            </div>
                        </li>
                        <li class="list-group-item">
                           <div class="row">
                            <div class="col-5 text-end">
                                <span class="text-secondary">Añada:</span>
                            </div>
                            <div class="col text-end">
                                <strong>
                                    {{ selected_taking.year }}
                                </strong>
                            </div>
                           </div>
                        </li>
                        <li class="list-group-item">
                           <div class="row">
                            <div class="col-5 text-end">
    <span class="text-secondary">Caducidad:</span>
                            </div>
                            <div class="col text-end">
                                <strong 
                                    v-if="selected_taking.date_expiry">
                                    {{ new Date (selected_taking.date_expiry).toLocaleString('es-EC').substring(0,10)}}
                                </strong>
                            </div>
                           </div>

                        </li>
                    </ul>
                    <div class="card-body">
                        <div class="row">
                            <div class="col text-center">
                                <button class="btn btn-secondary" @click="showReport">
                                <i class="fas fa-times"></i> Cerrar
                            </button>
                            </div>
                            <div class="col text-center">
                                <button class="btn btn-danger" @click="removeItem">
                                <i class="fas fa-eraser"></i> Eliminar
                            </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { utils, writeFile } from 'xlsx';

export default {
    emits:['sendReport'],
    name: 'ReportTaking',
    props: {
        taking: {
            type: Object,
            default:null,
            required: true
        },
        team: {
            type: Object,
            default: null,
            required: true
        },
        user: {
            type: Object,
            default: null,
            required: true
        },
        server_status: {
            type: Object,
            default: null,
            required: true
        },
        report: {
            type: Array,
            default: null,
            required: true
        },
        base_url: {
            type: String,
            default: null,
            required: true
        },
    }, data() {
        return {
            selected_taking: null,
            show_taking: false,
            show_report: true,
            confirm_report_send: false,
            class_sync_btn: 'btn-primary',
            message_button: 'Sincronizar Datos',
            default_picture: this.base_url + '/static/img/generic_product.png',
        };
    }, methods: {
        showTaking(item) {
            this.selected_taking = item;
            this.show_report = false;
            this.show_taking = true;
        }, showReport() {
            this.show_report = true;
            this.show_taking = false;
        }, removeItem() {
            this.$emit('removeItem', this.selected_taking);
            this.showReport();
        }, sendReport() {
            if (this.confirm_report_send) {
                this.disable_button_send = true;
                this.downloadReport();
                return this.$emit('sendReport');
            }
            this.confirm_report_send = true;
            this.class_sync_btn = 'btn-success';
            this.message_button = 'Confirmar Reporte';
        },downloadReport(){
            let report_json = this.report.map(item=>{
                return {
                    'PK': item.pk,
                    'ID Team': this.team.pk,
                    'token': this.team.fields.token_team,
                    'Cuenta Contable': item.product.fields.account_code,
                    'Producto': item.product.fields.name,
                    'Cajas': item.taking_total_boxes,
                    'Unidades': item.taking_total_bottles,
                    'Total UND': (
                        item.taking_total_boxes 
                        * item.product.fields.quantity_per_box 
                    ) + item.taking_total_bottles,
                    'Añada': item.year,
                    'Caducidad': item.date_expiry,
                    'Novedad': item.notes,
                }
            })
            const wb = utils.book_new();
            const ws = utils.json_to_sheet(report_json);
            utils.book_append_sheet(wb, ws, 'Reporte');
            let filename = (
                this.user.fields.username +
                '-' + this.taking.fields.name + 
                '-' + this.taking.fields.created + 
                '-' + '.xlsx'
                );
            writeFile(wb,filename);
        }
    }, computed: {
        total_boxes() {
            const initialValue = 0;
            const total = this.report.reduce((last_sum, current) => {
                return last_sum + current.taking_total_boxes;
            }, initialValue);
            return total;
        }, total_bottles() {
            const sheet = this.report;
            const initialValue = 0;
            const total = this.report.reduce((last_sum, current) => {
                return last_sum + current.taking_total_bottles;
            }, initialValue);
            return total
        },
    },
}
</script>
<style>
table.mi_table td{
    border: 0.20px solid;
}
</style>