app.component('report-taking', {
    template: /* vue-html */`
    <div class="card card-outline card-primary">
            <div class="card-header">
                <div v-if="report.length && show_report">
                    <div class="row">
                        <div class="col text-center">
                            <i class="fas fa-table"></i>
                            <strong class="text-primary h5">
                                Reporte Toma <small class="text-info">[{{ report.length }}] items</small>
                                <br>
                            </strong>
                            <i class="fas fa-close"></i>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <table class="mi_table" style="width:100%;">
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
                                        <td class="text-center">{{ index+1 }}</td>
                                        <td class=""> <i class="fas fa-exclamation-triangle text-warning" v-if="item.notes"></i> {{ item.product.fields.name }}</td>
                                        <td class="text-right">{{ item.taking_total_boxes }}</td>
                                        <td class="text-right">{{ item.taking_total_bottles }}</td>
                                    </tr>
                                    <tr class="bg-secondary">
                                        <td class="text-right" colspan="2"> <strong>TOTALES</strong></td>
                                        <td class="text-right"><strong v-text="total_boxes"></strong> </td>
                                        <td class="text-right"><strong v-text="total_bottles"></strong></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <button class="btn btn-block btn-primary" @click=sendDataReprot()>
                                <i class="fas fa-sync"></i> Sincronizar Datos
                                <small>
                                    [<span text="report.length"></span> items]
                                </small>
                            </button>
                        </div>
                    </div>
                </div>
                <div v-if="!report.length" class="text-center">
                    <strong class="text-info H2">SIN DATOS</strong>
                </div>
                <div v-if="show_taking" class="bg-white">
                    <div class="row h5">
                        <div class="col text-center text-primary">
                            {{ selected_taking.product.fields.name }}
                            <br>
                            <span class="badge badge-primary">{{selected_taking.product.fields.quantity_per_box}} x Caja</span>
                        </div>
                    </div>
                    <div class="row h4 text-right">
                        <div class="col">
                            <span class="text-secondary">Cajas:</span>
                        </div>
                        <div class="col">
                            <strong>
                                {{ selected_taking.taking_total_boxes }}
                            </strong>
                        </div>
                    </div>
                    <div class="row h4 text-right">
                        <div class="col">
                            <span class="text-secondary">Botellas:</span>
                        </div>
                        <div class="col">
                            <strong>
                                {{ selected_taking.taking_total_bottles }}
                            </strong>
                        </div>
                    </div>
                      <div class="row h6 border">
                        <div class="col">
                            <span v-if="selected_taking.notes" v-text="selected_taking.notes"></span>
                            <span v-else="" class="text-secondary">Sin Novedad</span>
                        </div>
                    </div>
                    <div class="row text-center">
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
                    <br/>
                </div>

            </div>
        </div>`,
        props:['user', 'report', 'server_status', 'csrf_token'],
        emits:['removeitem'],
        data() {
            return {
                selected_taking: null,
                show_taking: false,
                show_report:true,
            };
        },methods:{
            changeView(){

            },showTaking(item){
                this.selected_taking = item;
                this.show_report=false;
                this.show_taking=true;
            },showReport(){
                this.show_report=true;
                this.show_taking=false;
            },removeItem(){
                this.$emit('removeitem', this.selected_taking);
                this.showReport();
            },
        },computed:{
            total_boxes(){
                const initialValue = 0;
                const total= this.report.reduce((last_sum, current)=>{
                    return last_sum + current.taking_total_boxes;
                }, initialValue);
                return total;
            },total_bottles(){
                const initialValue = 0;
                const total =  this.report.reduce((last_sum, current)=>{
                    return last_sum + current.taking_total_bottles;
                }, initialValue);
                return total
            },
        },
});