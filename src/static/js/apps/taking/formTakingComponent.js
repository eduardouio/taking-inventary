app.component('form-taking', {
    template: /* vue-html */`
    <div class="card card-outline card-success">
            <div class="card-header">
                <div class="row align-middle text-center">
                    <div class="col h5 text-success">
                        {{ current_item.fields.name }}
                    </div>
                </div>
                 <div class="row">
                        <div class="col text-center">
                            <div class="col">
                                <img :src="default_picture" class="img-fluid img-thumbnail">
                            </div>
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
        props:['current_item','csfr_token','server_status','report'],
        emits:['changeview'],
        data() {
            return{
                current_taking: {
                    pk:null,
                    taking: taking.pk,
                    account_code: null,
                    taking_total_boxes:0,
                    taking_total_bottles:0,
                    notes:null,
                },
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
                this.report.push(this.current_taking);
                this.changeView();
            }
         },mounted(){
            if( this.current_item.fields.image_front){
                this.default_picture = '/media/' + this.current_item.fields.image_front
            }
        }
});