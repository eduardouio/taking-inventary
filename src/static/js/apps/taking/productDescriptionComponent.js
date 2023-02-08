app.component('product-description', {
    template: /* vue-html */`
    <div class="card card-outline card-success">
            <div class="card-header">
                <div class="row">
                    <div class="col text-center">
                        <strong class="text-secondary h6">{{ current_item.fields.name }}</strong>
                        <br>
                        <span class="text-primary">{{ current_item.fields.ean_13_code }}</span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-2 align-middle">
                        <i class="fas fa-eye btn btn-sm btn-outline-info" @click="show_product = !show_product"></i>
                    </div>
                    <div class="col">
                    <button class="btn btn-success btn-block" @click="changeView('taking_form')">
                            <i class="fas fa-clipboard-check"></i>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            Ingresar Toma
                </button>
                <br/>
                    </div>
                </div>
                <div id="detail">
                    <div class="row" v-if="show_product">
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
                                    <th class="bg-gradient-light text-right">Nombre:</th>
                                    <td v-text="current_item.fields.name"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Cod Contable:</th>
                                    <td v-text="current_item.fields.account_code"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Capacidad:</th>
                                    <td> <span v-text="current_item.fields.capacity"></span> <span v-text="current_item.fields.unit_measurement"></span> </td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">EAN 13:</th>
                                    <td v-text="current_item.fields.ean_13_code"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">EAN 14:</th>
                                    <td v-text="current_item.fields.ean_14_code"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Tipo:</th>
                                    <td v-text="current_item.fields.type_product"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">UND Venta:</th>
                                    <td v-text="current_item.fields.sale_unit_measurement"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Grado Alc.:</th>
                                    <td v-text="current_item.fields.alcoholic_strength"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Dim Caja:</th>
                                    <td v-text="current_item.fields.box_dimensions"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Dim Product:</th>
                                    <td v-text="current_item.fields.product_dimensions"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">COD ICE:</th>
                                    <td v-text="current_item.fields.ice_code"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Cantidad Caja:</th>
                                    <td v-text="current_item.fields.quantity_per_box"></td>
                                </tr>
                                <tr>
                                    <th class="bg-gradient-light text-right">Registro Sanitario:</th>
                                    <td v-text="current_item.fields.health_register"></td>
                                </tr>
                                <tr>
                                    <td colspan="2" class="text-center bg-gradient-light">
                                        <button class="btn btn-primary btn-block" @click="changeView('product_form')">
                                            <i class="fas fa-box"></i>
                                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                            Actualiza Ficha
                                        </button>
                                    </td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>`,
        props:['current_item',],
        emits:['changeview',],
        data() {
            return{
                show_product: false,
                default_picture: '/static/img/generic_product.png',
                class_bagded_front: 'badge-primary',
                class_bagded_back: 'badge-light',
            };
        },methods: {
            switchImage(option){
                if (option === 'front' && this.current_item.fields.image_front){
                    this.default_picture = '/media/' + this.current_item.fields.image_front;
                    this.class_bagded_front = 'badge-primary'
                    this.class_bagded_back = 'badge-light'
                }else if (option === 'back' && this.current_item.fields.image_back){
                    this.default_picture = '/media/' + this.current_item.fields.image_back;
                    this.class_bagded_back = 'badge-primary'
                    this.class_bagded_front = 'badge-light'
                }else{
                    this.default_picture = '/static/img/generic_product.png';
                }
            },
            changeView(view_name){
                this.$emit('changeview', view_name)
            },
        },mounted(){
            if( this.current_item.fields.image_front){
                this.default_picture = '/media/' + this.current_item.fields.image_front
            }
        },
        
})