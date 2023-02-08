app.component('form-taking', {
    template: /* vue-html */`
    <div class="card card-outline card-success">
            <div class="card-header">
                <div class="row align-middle text-center">
                    <div class="col text-secondary h6">
                        {{ current_item.fields.name }} 
                        <br/>
                        <small class="text-primary">[{{current_item.fields.quantity_per_box}} x Caja] 
                        &nbsp;|&nbsp; 
                        <span class="text-primary">{{ current_item.fields.ean_13_code }}</span></small> 
                        &nbsp;|&nbsp;
                        <i class="fas fa-eye btn btn-sm btn-outline-info" @click="show_product = !show_product"></i>
                    </div>
                </div>
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
                <div class="row align-middle">
                    <div class="col text-center">
                        <i class="fas fa-check-square"></i>
                        <strong class="text-success">Ingresa Existencias</strong>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <div class="row">
                            <div class="col-4 text-right align-middle">Cajas:</div>
                            <div class="col">
                                <input type="number" class="form-control taking-number" v-model="current_taking.taking_total_boxes" onfocus="this.value=''">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-4 text-right align-middle">Botellas:</div>
                            <div class="col">
                                <input type="number" class="form-control taking-number" v-model="current_taking.taking_total_bottles" onfocus="this.value=''">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-4 text-right align-middle">Observaciones:</div>
                            <div class="col">
                                <textarea class="form-control taking-text" v-model="current_taking.notes" onfocus="this.value=''"></textarea>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <button class="btn btn-block btn-success" @click="addReport">
                                    <i class="fas fa-plus"></i> Agregar Toma</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>`,
        props:['current_item','report'],
        emits:['changeview'],
        data() {
            return{
                current_taking: {
                    pk:null,
                    product:null,
                    taking: taking.pk,
                    account_code: null,
                    taking_total_boxes:0,
                    taking_total_bottles:0,
                    notes:null,
                },
                show_product: false,
                default_picture: '/static/img/generic_product.png',
                class_bagded_front: 'badge-primary',
                class_bagded_back: 'badge-light',
            }
        },
        methods: {
            changeView(){
                this.$emit('changeview', 'search_form')
            },switchImage(option){
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
            },addReport(){
                if (typeof(this.current_taking.taking_total_boxes) != 'number'){
                    this.current_taking.taking_total_boxes = 0;
                }
                if (typeof(this.current_taking.taking_total_bottles) != 'number'){
                    this.current_taking.taking_total_bottles = 0;
                }
                let sum = this.current_taking.taking_total_boxes + this.current_taking.taking_total_bottles
                if(!sum){
                    alert('Valores en cero');
                    return false;
                }
                this.current_taking.product = this.current_item;
                this.report.push(this.current_taking);
                this.changeView();
            }
         },mounted(){
            if( this.current_item.fields.image_front){
                this.default_picture = '/media/' + this.current_item.fields.image_front
            }
        }
});