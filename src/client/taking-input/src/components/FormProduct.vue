<template>
 <div class="card card-outline card-warning">
        <div class="card-header">
            <div class="row">
                <div class="col text-center">
                    <strong class="text-warning" v-text="current_item.name"></strong>
                </div>
            </div>
            <div class="row">
                <div class="col text-center">
                    <img :src="default_picture" class="img-fluid img-thumbnail">
                </div>
            </div>
            <div class="row h5">
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
                            <div class="form-group">
                                <label>Nombre</label>
                                <input type="text" class="form-control" readonly v-model="current_item.name">
                            </div>
                            <div class="form-group">
                                <label>Typo Producto</label>
                                    <select class="form-control" v-model="current_item.type_product">
                                    <option value="ACCESORIO">ACCESORIO</option>
                                    <option value="AGUA TONICA">AGUA TÓNICA</option>
                                    <option value="ALIMENTO">ALIMENTO</option>
                                    <option value="BAJATIVO">BAJATIVO</option>
                                    <option value="BEBIDAS AZUCARADAS">BEBIDAS AZUCARADAS</option>
                                    <option value="CHAMPAGNE">CHAMPAGNE</option>
                                    <option value="MUEBLE">MUEBLE</option>
                                    <option value="PISCO">PISCO</option>
                                    <option value="RON">RON</option>
                                    <option value="SANGRIA">SANGRIA</option>
                                    <option value="VINO BLANCO">VINO BLANCO</option>
                                    <option value="VINO ESPUMOSO">VINO ESPUMOSO</option>
                                    <option value="VINO TINTO">VINO TINTO</option>
                                    <option value="WHISKY">WHISKY</option>
                                    <option value="OTRO">OTRO Bien</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="">EAN 13</label>
                                <input type="text" class="form-control" v-model="current_item.ean_13_code" :disabled="!current_item.ean_13_code == ''">
                            </div>
                            <div class="form-group">
                                <label for="">EAN 14</label>
                                <input type="text" class="form-control" v-model="current_item.ean_14_code" :disabled="!current_item.ean_14_code == ''">
                            </div>
                            <div class="form-group">
                                <label>Capacidad</label>
                                <input type="number" class="form-control" v-model="current_item.capacity" :disabled="current_item.capacity != 0">
                            </div>
                            <div class="form-group">
                                <label>Unidad Medida</label>
                                <input  type="text" class="form-control" v-model="current_item.unit_measurement" disabled>
                            </div>
                            <div class="form-group">
                                <label>Dimensiones Producto CM</label>
                                <input type="text" class="form-control" v-model="current_item.product_dimensions" placeholder="largo X alto X ancho">
                            </div>
                            <div class="form-group">
                                <label>Dimensiones Caja Madre CM</label>
                                <input type="text" class="form-control" v-model="current_item.box_dimensions" placeholder="largo X alto X ancho">
                            </div>
                            <div class="form-group">
                                <label>Observaciones</label>
                                <textarea v-model="current_item.notes" class="form-control"></textarea>
                            </div>
                            <hr/>

                        </div>
                    </div>
                    <div class="row">
                        <button class="btn btn-block btn-warning" @click="updateProduct"> <i class="fas fa-box"></i> &nbsp;&nbsp; Actualizar</button>
                    </div>
            </div>
        </div>
</template>
<script>
export default {
    name: "FormProduct",
    emits: ['updateProduct'],
    props: {
        current_item: {
            type: Object,
            required: true
        },
    },
    data() {
        return {
            default_picture: '/static/img/default_product.png',
            current_picture: 'front',
            class_bagded_front: 'badge-primary',
            class_bagded_back: 'badge-light',
        }
    },methods: {
    switchImage(option) {
        if (option === 'front' && this.current_item.image_front) {
            this.default_picture = '/media/' + this.current_item.image_front;
            this.class_bagded_front = 'badge-primary'
            this.class_bagded_back = 'badge-light'
        } else if (option === 'back' && this.current_item.image_back) {
            this.default_picture = '/media/' + this.current_item.image_back;
            this.class_bagded_back = 'badge-primary'
            this.class_bagded_front = 'badge-light'
        } else {
            this.default_picture = '/static/img/generic_product.png';
        }
    }, updateProduct() {
       this.$emit('updateProduct', this.current_item);
    },
},
    computed: {
        class_bagded_front() {
            return {
                'badge-warning': this.current_picture == 'front',
                'badge-secondary': this.current_picture != 'front',
            }
        },
        class_bagded_back() {
            return {
                'badge-warning': this.current_picture == 'back',
                'badge-secondary': this.current_picture != 'back',
            }
        }
    }, mounted() {
    if (this.current_item.image_front) {
        this.default_picture = '/media/' + this.current_item.image_front
    }
},
}
</script>