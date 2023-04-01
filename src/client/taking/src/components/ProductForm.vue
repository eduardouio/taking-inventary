<template>
 <div class="card card-outline card-warning">
        <div class="card-header">
            <div class="row">
                <div class="col text-center">
                    <strong class="text-warning" v-text="current_item.fields.name"></strong>
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
                                <input type="text" class="form-control" readonly v-model="current_item.fields.name">
                            </div>
                            <div class="form-group">
                                <label>Typo Producto</label>
                                    <select class="form-control" v-model="current_item.fields.type_product">
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
                                <input type="text" class="form-control" v-model="current_item.fields.ean_13_code" :disabled="!current_item.fields.ean_13_code == ''">
                            </div>
                            <div class="form-group">
                                <label for="">EAN 14</label>
                                <input type="text" class="form-control" v-model="current_item.fields.ean_14_code" :disabled="!current_item.fields.ean_14_code == ''">
                            </div>
                            <div class="form-group">
                                <label>Capacidad</label>
                                <input type="number" class="form-control" v-model="current_item.fields.capacity" :disabled="current_item.fields.capacity != 0">
                            </div>
                            <div class="form-group">
                                <label>Unidad Medida</label>
                                <input  type="text" class="form-control" v-model="current_item.fields.unit_measurement" disabled>
                            </div>
                            <div class="form-group">
                                <label>Dimensiones Producto CM</label>
                                <input type="text" class="form-control" v-model="current_item.fields.product_dimensions" placeholder="largo X alto X ancho">
                            </div>
                            <div class="form-group">
                                <label>Dimensiones Caja Madre CM</label>
                                <input type="text" class="form-control" v-model="current_item.fields.box_dimensions" placeholder="largo X alto X ancho">
                            </div>
                            <div class="form-group">
                                <label>Observaciones</label>
                                <textarea v-model="current_item.fields.notes" class="form-control"></textarea>
                            </div>
                            <hr/>
                            <button class="btn btn-block btn-warning" @click="updateProduct"> <i class="fas fa-box"></i> &nbsp;&nbsp; Actualizar</button>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
export default {
    name: "ProductForm",
    props: {
        current_item: {
            type: Object,
            default: () => {
                return {
                    fields: {
                        name: '',
                        type_product: '',
                        ean_13_code: '',
                        ean_14_code: '',
                        capacity: 0,
                        unit_measurement: '',
                        product_dimensions: '',
                        box_dimensions: '',
                        notes: '',
                        picture_front: '',
                        picture_back: '',
                    }
                }
            }
        }
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
    }, updateProduct() {
        const formData = new FormData()
        formData.append('product', JSON.stringify(this.current_item));
        let xhrequest = new XMLHttpRequest()
        xhrequest.open(
            'POST',
            '/product/update/'
        );
        xhrequest.setRequestHeader('X-CSRFToken', this.csrf_token);
        xhrequest.send(formData)
        xhrequest.onload = () => {
            if (xhrequest.status == 201) {
                this.selectProduct();
            } else {

            }
        };
    }, selectProduct() {
        this.$emit('selectproduct', this.current_item);
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
    if (this.current_item.fields.image_front) {
        this.default_picture = '/media/' + this.current_item.fields.image_front
    }
},
}
</script>