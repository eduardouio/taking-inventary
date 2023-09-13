<template>
    <div class="card card-outline card-success mt-1">
        <div class="card-header">
            <div class="row align-middle text-center">
                <div class="col h6">
                    {{ current_item.name }}
                    <br />
                    <small class="text-primary">
                        CAPACIDAD: {{ current_item.capacity }} {{ current_item.unit_measurement }}
                    </small>
                    <br />
                    <small class="text-primary">[{{ current_item.quantity_per_box }} x Caja]
                        &nbsp;|&nbsp;
                        <span class="text-primary">{{ current_item.ean_13_code }}</span></small>
                </div>
            </div>
            </div>
            <div class="card-body">
                    <div class="row mt-2 mb-2">
                        <div class="col text-center">
                        <img
                        :src= "current_item.image_front ? baseURL + current_item.image_front: default_picture"
                        class="img-fluid img-thumbnail"
                        >
                    </div>
                    </div>
                    <div class="row">
                        <div class="col-5 text-end">CAJAS:</div>
                        <div class="col">
                            <input
                                type="number"
                                class="form-control taking-number text-end"
                                autofocus
                                v-model="current_taking.taking_total_boxes"
                                onfocus="this.value=''"
                                >
                        </div>
                    </div>
                    <div class="row mt-1">
                        <div class="col-5 text-end">UNIDADES:</div>
                        <div class="col">
                            <input type="number" class="form-control taking-number text-end" autofocus
                                v-model="current_taking.taking_total_bottles" onfocus="this.value=''">
                        </div>
                    </div>
               <div class="row mt-1">
                        <div class="col-5 text-end">AÑADA:</div>
                            <div class="col">
                                <input type="number" class="form-control taking-number text-end"
                                    v-model="current_taking.year">
                            </div>
                </div>
            <div class="row mt-1">
                <div class="col-5 text-end">CADUCIDAD:</div>
                    <div class="col">
                        <input type="date" class="form-control taking-number text-end"
                            v-model="current_taking.date_expiry">
                    </div>
            </div>
            <div class="row mt-1">
                <div class="col-3 text-end">NOTAS:</div>
                <div class="col">
                    <textarea class="form-control taking-text" v-model="current_taking.notes"></textarea>
                </div>
            </div>
        </div>
        <div class="card-footer mt-1 bg-ligth">
            <div class="row text-center">
                <div class="col-6">
                    <button class="btn btn-block btn-lg btn-secondary" @click="switchView">
                        <i class="fas fa-arrow-left"></i> Regresar</button>
                </div>
                <div class="col-6">
                    <button class="btn btn-block btn-lg btn-success" @click="addReport">
                        <i class="fas fa-save"></i> Guardar</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import appConfig from '../appConfig'

export default {
    name: 'FormTaking',
    props: {
        current_item: {
            type: Object,
            default: () => {},
            required: true,
        },base_url: {
            type: String,
            default: () => {},
            required: true,
        },report: {
            type: Array,
            default: () => {},
            required: true,
        }
    },
    emits: ['switchView'],
    data() {
        return {
            current_taking: {
                pk: null,
                product: null,
                taking_total_boxes: 0,
                taking_total_bottles: 0,
                date_expiry: null,
                year: null,
                notes: null,
            },
            show_product: true,
            default_picture: appConfig.defaultPicture,
            class_bagded_front: 'badge-primary',
            class_bagded_back: 'badge-light',
            baseURL : appConfig.apiBaseUrl,
        }
    },
    methods: {
        switchView() {
            this.$emit('switchView', 'search_form')
        }, addReport() {
            if (typeof (this.current_taking.taking_total_boxes) != 'number') {
                this.current_taking.taking_total_boxes = 0;
            }
            if (typeof (this.current_taking.taking_total_bottles) != 'number') {
                this.current_taking.taking_total_bottles = 0;
            }
            this.current_taking.product = this.current_item;
            this.current_taking.pk = this.current_item.pk;
            this.report.push(this.current_taking);
            this.switchView();
        }
    }, mounted() {
        if (this.current_item.image_front) {
            this.default_picture = this.base_url + '/media/' + this.current_item.image_front
        }
    },updated(){
        if (this.current_taking.taking_total_boxes <= 0) {
            this.current_taking.taking_total_boxes = "";
        }
        if (this.current_taking.taking_total_bottles <= 0) {
            this.current_taking.taking_total_bottles = "";
        }
        if (this.current_taking.year <= 0) {
            this.current_taking.year = "";
        }
    }
}
</script>
<style>
    .taking-number{
        font-size: 1.2em;
    }
    .taking-number:fo   cus{
        background-color: #96e4f780;
    }
    .taking-text:focus{
        background-color: #96e4f780;
    }
</style>