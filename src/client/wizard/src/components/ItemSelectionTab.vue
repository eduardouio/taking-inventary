<template>
    <div class="row mt-2">
                    <h5 class="mt-2">PERSONALIZAR ITEMS TOMA</h5>
                    <div class="col bg-light">
                        <div class="row">
                            <div class="col-8 mt-2">
                                <table class="table table-bordered table-hover table-condesed mi_table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Tipo</th>
                                            <th><i class="fas fa-cogs"></i></th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(category,idx) in categories" :key="category.category" @click="category.selected = !category.selected">
                                            <td>{{ idx + 1 }}</td>
                                            <td class="text-start">{{ category.category }}</td>
                                            <td class="text-success">
                                                
                                                    <i class="fa-solid fa-minus text-danger" v-if="category.selected"></i>
                                                    <i class="fa-solid fa-plus" v-else></i>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="col-4 mt-2">
                                <div class="card">
                                    <div class="card-body">
                                        <h5 class="card-title">Items Seleccionados</h5>
                                        <p class="card-text">
                                        <ul class="list-group text-start">
                                            <li class="list-group-item p-1">Licores</li>
                                            <li class="list-group-item p-1">Alimentos</li>
                                        </ul>
                                        </p>
                                    </div>
                                </div>
                                <br />
                            </div>
                        </div>
                               <div class="row mt-3">
                                <div class="col text-start">
                                    <button class="btn btn-primary btn-sm" @click="showView(3)">
                                        <i class="fa-solid fa-chevron-left"></i> Anterior
                                    </button>
                                </div>
                                <div class="col text-end">
                                    <button class="btn btn-success btn-sm" @click="showView(5)">
                                        Siguiente<i class="fa-solid fa-chevron-right"></i>
                                    </button>
                            </div>
                            </div>
                            <br/>
                    </div>

                </div>
</template>

<script>
export default {
    name: 'ItemSelectionTab',
    emits: ['showView'],
    props: {
        type_products: {
            type: Object,
            required: true
        }
    },data(){
        return{
            all_type_products: [],
            categories: [],
            selected_categories: [],
        }
    },
    methods: {
        showView(view) {
            this.$emit('showView', view);
        },showView(view) {
            this.$emit("showView", view);
        },selectCategory(category){
            // agregamos la categoria a selected_categories
            
        },
    },mounted(){
        let my_categories;
        this.all_type_products = [...this.type_products];

        my_categories = this.all_type_products.map((item)=>{
            return item.type_product.split(';')[0];
        });

        this.categories = [...new Set(my_categories)];
    },
}
</script>