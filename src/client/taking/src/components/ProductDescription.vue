<template>
    <div class="card">
        <div class="card-header">
            <div class="row">
                <div class="col text-center">
                    <strong class="text-secondary h6">{{ current_item.fields.name }}</strong>
                    <br>
                    <span class="text-primary">{{ current_item.fields.ean_13_code }}</span>
                </div>
            </div>
            <div class="card-body">
            <div class="row">
                <div class="d-grid gap-2">
                    <button class="btn btn-success btn-block" @click="changeView('taking_form')">
                        <i class="fas fa-clipboard-check"></i>
                        Ingresar Toma
                    </button>
                    <br />
                </div>
            </div>
            <div id="detail">
                <div class="row">
                    <div class="col text-center">
                        <div class="col">
                            <img :src="default_picture" class="img-fluid img-thumbnail">
                        </div>
                    </div>
                </div>
                <div class="row h5" v-if="show_product">
                    <div class="col text-center">
                        <span class="badge" :class="class_bagded_front" @click="switchImage('front')">
                            Fontal
                        </span>
                    </div>
                    <div class="col text-center">
                        <span class="badge" :class="class_bagded_back" @click="switchImage('back')">
                            Posterior
                        </span>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <table class="table table-bordered table-compact">
                            <tr>
                                <th class="bg-light bg-gradient text-end">Nombre:</th>
                                <td v-text="current_item.fields.name"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Cod Contable:</th>
                                <td v-text="current_item.fields.account_code"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Capacidad:</th>
                                <td> <span v-text="current_item.fields.capacity"></span> <span
                                        v-text="current_item.fields.unit_measurement"></span> </td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">EAN 13:</th>
                                <td v-text="current_item.fields.ean_13_code"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">EAN 14:</th>
                                <td v-text="current_item.fields.ean_14_code"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Tipo:</th>
                                <td v-text="current_item.fields.type_product"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">UND Venta:</th>
                                <td v-text="current_item.fields.sale_unit_measurement"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Grado Alc.:</th>
                                <td v-text="current_item.fields.alcoholic_strength"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Dim Caja:</th>
                                <td v-text="current_item.fields.box_dimensions"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Dim Product:</th>
                                <td v-text="current_item.fields.product_dimensions"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">COD ICE:</th>
                                <td v-text="current_item.fields.ice_code"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Cantidad Caja:</th>
                                <td v-text="current_item.fields.quantity_per_box"></td>
                            </tr>
                            <tr>
                                <th class="bg-light bg-gradient text-end">Registro Sanitario:</th>
                                <td v-text="current_item.fields.health_register"></td>
                            </tr>

                        </table>
                    </div>
                </div>
                <div class="row">
                    <div class="d-grid gap-2">
                          <button 
                                            class="btn btn-primary btn-block"
                                            @click="$event => changeView('product_form')">
                                            <i class="fas fa-box"></i>
                                                Actualiza Ficha
                                        </button>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "ProductDescription",
    props: {
        current_item: {
            type: Object,
            default: () => {}
        },
        base_url: {
            type: String,
            default: ''
        }
    },emit: ['changeView'],
    data() {
        return {
            show_product: false,
            default_picture: this.base_url + '/static/img/generic_product.png',
            class_bagded_front: 'badge rounded-pill text-bg-primary',
            class_bagded_back:'badge rounded-pill text-bg-light',
        }
    }, methods: {
        switchImage(option) {
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
        },
        changeView(view_name) {
            this.$emit('changeview', view_name)
        },
    }, mounted() {
        if (this.current_item.fields.image_front) {
            this.default_picture = '/media/' + this.current_item.fields.image_front
        }
    },
}
</script>
<style>
.table-compact td, .table-compact th {
    padding: .05 rem;
    vertical-align: middle;
    background-color: white;
}


</style>