<template>
    <div class="card card-outline card-success mt-1">
        <div class="card-header">
            <div class="row align-middle text-center">
                <div class="col h6">
                    {{ current_item.fields.name }}
                    <br />
                    <small class="text-primary">
                        CAPACIDAD: {{ current_item.fields.capacity }} {{ current_item.fields.unit_measurement }}
                    </small>
                    <br />
                    <small class="text-primary">[{{ current_item.fields.quantity_per_box }} x Caja]
                        &nbsp;|&nbsp;
                        <span class="text-primary">{{ current_item.fields.ean_13_code }}</span></small>
                </div>
            </div>
            <div class="row align-middle mt-1">
                <div class="col text-center">
                    <i class="fas fa-check-square"></i>
                    <strong class="text-success">Ingresa Existencias</strong>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-4 text-center">
                    <img :src="default_picture" class="img-fluid img-thumbnail">
                </div>
                <div class="col">
                    <div class="row">
                        <div class="col-5 text-end">Cajas:</div>
                        <div class="col">
                            <input type="number" class="form-control taking-number text-end"
                                v-model="current_taking.taking_total_boxes" onfocus="this.value=''">
                        </div>
                    </div>
                    <div class="row mt-1">
                        <div class="col-5 text-end">Unds:</div>
                        <div class="col">
                            <input type="number" class="form-control taking-number text-end"
                                v-model="current_taking.taking_total_bottles" onfocus="this.value=''">
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-1">
                <div class="col-5 text-end">Vencimiento:</div>
                    <div class="col">
                        <input type="date" class="form-control taking-number text-end"
                            v-model="current_taking.date_expiry">
                    </div>
            </div>
            <div class="row mt-1">
                    <div class="col-5 text-end">Añada:</div>
                        <div class="col">
                            <input type="year" class="form-control taking-number text-end"
                                v-model="current_taking.year">
                        </div>
            </div>
            <div class="row mt-1">
                <div class="col-3 text-end">Notas:</div>
                <div class="col">
                    <textarea class="form-control taking-text" v-model="current_taking.notes"></textarea>
                </div>
            </div>
            <div class="row mt-2">
                <div class="col">
                    <button class="btn btn-block btn-success" @click="addReport">
                        <i class="fas fa-plus"></i> Agregar Toma</button>
                </div>
            </div>
        </div>
</div></template>
<script>
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
    emits: ['change-view'],
    data() {
        return {
            current_taking: {
                pk: null,
                product: null,
                account_code: null,
                taking_total_boxes: 0,
                taking_total_bottles: 0,
                date_expiry: null,
                year: null,
                notes: null,
            },
            show_product: true,
            default_picture: this.base_url +  '/static/img/generic_product.png',
            class_bagded_front: 'badge-primary',
            class_bagded_back: 'badge-light',
        }
    },
    methods: {
        changeView() {
            this.$emit('changeView', 'search_form')
        }, switchImage(option) {
            if (option === 'front' && this.current_item.fields.image_front) {
                this.default_picture = '/media/' + this.current_item.fields.image_front;
                this.class_bagded_front = 'badge-primary'
                this.class_bagded_back = 'badge-light'
            } else if (option === 'back' && this.current_item.fields.image_back) {
                this.default_picture = '/media/' + this.current_item.fields.image_back;
                this.class_bagded_back = 'badge-primary'
                this.class_bagded_front = 'badge-light'
            } else {
                this.default_picture = '/static/img/generic_product.png';
            }
        }, addReport() {
            if (typeof (this.current_taking.taking_total_boxes) != 'number') {
                this.current_taking.taking_total_boxes = 0;
            }
            if (typeof (this.current_taking.taking_total_bottles) != 'number') {
                this.current_taking.taking_total_bottles = 0;
            }
            let sum = this.current_taking.taking_total_boxes + this.current_taking.taking_total_bottles
            if (!sum) {
                alert('Valores en cero');
                return false;
            }
            this.current_taking.product = this.current_item;
            this.report.push(this.current_taking);
            this.changeView();
        }
    }, mounted() {
        if (this.current_item.fields.image_front) {
            this.default_picture = this.base_url + '/media/' + this.current_item.fields.image_front
        }
    }
}
</script>
<style>
    .taking-number{
        font-size: 1.2em;
    }
    .taking-number:focus{
        font-size: 1.8em;
        background-color: #96e4f780;
    }
    .taking-text:focus{
        background-color: #96e4f780;
    }
</style>