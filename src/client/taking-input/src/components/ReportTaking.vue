<template>
    <div>
    <div class="card card-outline card-primary" v-if="show_section.report">
        <div class="card-header">
            <div v-if="report.length && show_report">
                <div class="row mb-2 mt-2">
                    <div class="col text-center">
                        <i class="fas fa-table"></i>
                        <strong class="h6 mt-1 mb-1">
                            {{ taking.name }}
                            <small>[{{ report.length }}] items</small>
                        </strong>
                        <small class="badge bg-success mb-1" @click="switchView('taking_form')">
                            Toma Nro #{{ taking.id_taking }}
                        </small>
                        <br>
                        <button @click="downloadReport" class="btn btn-outline-success btn-sm">
                            <i class="fas fa-file-excel"></i> Descargar Reporte
                        </button>
                    </div>
                </div>
                <div class="row mt-1">
                    <div class="col">
                        <div class="table-responsive" style="height:25rem;">
                            <table class="table table-sm table-bordered table-striped " style="width:100%;">
                                <thead>
                                    <tr class="bg-dark text-white">
                                        <th class="text-center">#</th>
                                        <th class="text-center">PRODUCTO</th>
                                        <th class="text-center">CAJAS</th>
                                        <th class="text-center">UNDS</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(item, index) in report" :key="item.pk" @click="showTaking(item)">
                                        <td class="text-center">{{ index + 1 }}</td>
                                        <td class=""> <i class="fas fa-exclamation-triangle text-warning"
                                                v-if="item.notes"></i>
                                            {{ item.product.name }}</td>
                                        <td class="text-end">{{ item.taking_total_boxes }}</td>
                                        <td class="text-end">{{ item.taking_total_bottles }}</td>
                                    </tr>
                                    <tr class="bg-dark">
                                        <td class="text-end text-white" colspan="2"> <strong>TOTALES</strong></td>
                                        <td class="text-end text-white"><strong v-text="total_boxes"></strong> </td>
                                        <td class="text-end text-white"><strong v-text="total_bottles"></strong></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
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
                            <img :src="appConfig.apiBaseUrl + selected_taking.product.image_front ? appConfig.apiBaseUrl + selected_taking.product.image_front : default_picture"
                                class="card-img-top img-thumbnail" alt="Imagen Producto" style="width:12em; height:auto;">
                        </div>
                    </div>
                    <div class="card-body">
                        <h5 class="card-title text-center text-primary">{{ selected_taking.product.name }}</h5>
                        <p class="card-text border rounded p-1 text-info">
                            <span v-if="selected_taking.notes" class="h3" v-text="selected_taking.notes"></span>
                            <span v-else class="text-secondary h3">Sin Novedad</span>
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
                                    <strong v-if="selected_taking.date_expiry">
                                        {{ new Date(selected_taking.date_expiry).toLocaleString('es-EC').substring(0, 10) }}
                                    </strong>
                                </div>
                            </div>

                        </li>
                    </ul>
                    <div class="card-body">
                        <div class="row">
                            <div class="col text-center">
                                <button class="btn btn-secondary btn-lg" @click="showReport">
                                    <i class="fas fa-times"></i> Cerrar
                                </button>
                            </div>
                            <div class="col text-center">
                                <button class="btn btn-danger btn-lg" @click="removeItem">
                                    <i class="fas fa-eraser"></i> Eliminar
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="card" style="width: 100%;" v-if="show_section.response">
        <div class="card-header text-center">
            <h5 class="card-title text-success">Sincronización Completa</h5>
        </div>
    <div class="card-body">
        <p class="card-text">Lo siguiente fue sincronizado correctamente:</p>
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    <th scope="col">Typo</th>
                    <th scope="col">Cantidad</th>
                    <th scope="col">Detalle</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row">SKUs</th>
                    <td>{{ resumeReport.skus }}</td>
                    <td>Productos</td>
                </tr>
                <tr>
                    <th scope="row">Total Unds</th>
                    <td>{{ resumeReport.quantity }}</td>
                    <td>Unidades</td>
                </tr>
                <tr>
                    <th scope="row">Cajas</th>
                    <td>{{ resumeReport.taking_total_boxes }}</td>
                    <td>Cajas</td>
                </tr>
                <tr>
                    <th scope="row">Botellas</th>
                    <td>{{ resumeReport.taking_total_bottles }}</td>
                    <td>Unidades</td>
                </tr>
            </tbody>
        </table>
        <button>Nueva Yoma</button>
    </div>
</div>
</div>
</template>
<script>
import { utils, writeFile } from 'xlsx';
import appConfig from '../appConfig';

export default {
    name: 'ReportTaking',
    emits: ['switchView', 'removeItem'],
    props: {
        taking: {
            type: Object,
            default: null,
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
        show_view: {
            type: Object,
            default: null,
            required: true
        },
    }, data() {
        return {
            selected_taking: null,
            show_taking: false,
            show_report: true,
            class_sync_btn: 'btn-primary',
            message_button: 'Sincronizar Datos',
            disable_button_send: false,
            default_picture: appConfig.defaultPicture,
            appConfig: appConfig,
            resumeReport: null,
            show_section : {
                report: true,
                response: false,
            }
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
        }, async sendReport() {
            console.log('Enviando reporte');
            this.show_section.report = false;
            this.show_section.response = true;
            this.server_status.response = null;
            this.disable_button_send = true;

            const dataReport = {
                force: false,
                id_team: this.team.id_team,
                id_taking: this.taking.id_taking,
                token_team: this.team.token_team,
                report: this.report.map((item) => {
                    return {
                        id_product: item.product.id_product,
                        taking_total_boxes: item.taking_total_boxes,
                        taking_total_bottles: item.taking_total_bottles,
                        date_expiry: item.date_expiry,
                        year: item.year,
                        notes: item.notes,
                    }
                })
            }
            try {
                const response = await fetch(appConfig['syncUrl'], {
                    method: 'POST',
                    headers: appConfig['headers'],
                    body: JSON.stringify(dataReport),
                });

                if (response.status === 201) {
                    const responseData = await response.json();

                    const checkSums = {
                        skus: this.report.length,
                        quantity: this.report.reduce((acc, item) => {
                            return acc + (item.taking_total_boxes * item.product.quantity_per_box) + item.taking_total_bottles;
                        }, 0),
                        taking_total_boxes: this.report.reduce((acc, item) => {
                            return acc + item.taking_total_boxes;
                        }, 0),
                        taking_total_bottles: this.report.reduce((acc, item) => {
                            return acc + item.taking_total_bottles;
                        }, 0),
                    };

                    if (this.checkSums(checkSums, responseData)) {
                        this.show_section.report = false;
                        this.show_section.response = true;
                        this.server_status.issue_type = 'success';
                        this.server_status.message = 'Sincronizado correctamente';
                        this.server_status.response = responseData;
                        console.log('El reporte es correcto');
                    } else {
                        this.server_status.issue_type = 'error';
                        this.server_status.message = `Error en la sincronizacion`;
                        this.server_status.response = responseData;
                        this.show_section.report = true;
                        alert('Error en la sincronizacion');
                    }
                } else {
                    this.server_status.issue_type = 'error';
                    this.server_status.message = `Servidor desconectado ${response.statusText}`;
                }
            } catch (error) {
                this.server_status.response = null;
                this.server_status.issue_type = 'error';
                this.server_status.message = `Respuesta inesperada del servidor, verifique con el manager la sincronización ${error}`;
            }
        },checkSums(sendData, responseData) {
        console.log('Comprobamos los resultados del server');
        return (
            sendData.skus === responseData.skus &&
            sendData.quantity === responseData.quantity &&
            sendData.taking_total_boxes === responseData.taking_total_boxes &&
            sendData.taking_total_bottles === responseData.taking_total_bottles
        )
    },downloadReport() {
            let report_json = this.report.map(item => {
                return {
                    'PK': item.pk,
                    'ID Team': this.team.pk,
                    'token': this.team.token_team,
                    'Cuenta Contable': item.product.account_code,
                    'Producto': item.product.name,
                    'Cajas': item.taking_total_boxes,
                    'Unidades': item.taking_total_bottles,
                    'Total UND': (
                        item.taking_total_boxes
                        * item.product.quantity_per_box
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
                'Toma ' + this.taking.id_taking +
                '-' + this.taking.name +
                '-' + this.user.username +
                '-' + '.xlsx'
            );
            writeFile(wb, filename);
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
    table {
        font-size: 0.85rem;
    }
</style>