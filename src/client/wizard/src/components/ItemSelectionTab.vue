<template>
    <div class="row mt-2">
                    <h5 class="mt-2">PERSONALIZAR ITEMS TOMA</h5>
                    <div class="col bg-light">
                        <div class="row">
                            <div class="col-6 mt-2">
                                <table class="table table-bordered table-hover table-condesed mi_table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Tipo</th>
                                            <th><i class="fas fa-cogs"></i></th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(category,idx) in taking_data.categories" :key="category" @click="category.selected = !category.selected">
                                            <td>{{ idx + 1 }}</td>
                                            <td class="text-start">{{ category.category }}</td>
                                            <td class="text-center">
                                                <span :class="category.selected ? 'text-danger' : 'text-success'">
                                                    {{ category.selected ? 'Quitar' : 'Agregar'  }}
                                                </span>
                                            </td>
                                        </tr>
                                        <tr v-if="false">
                                            <td>{{ all_categories.length + 1 }}</td>
                                            <td class="text-start">SELECCIONAR PRODUCTOS</td>
                                            <td><i class="fa-solid fa-search"></i></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="col-6 mt-2">
                                <div class="card">
                                    <div class="card-body">
                                        <h5 class="card-title">Items Seleccionados</h5>
                                        <p class="card-text">
                                        <ul class="list-group text-start" v-for="category in selected_categories" :key="category">
                                            <li class="list-group-item p-1"> 
                                                <i class="fa-solid fa-minus text-danger"></i>
                                                {{ category.category }}
                                                <ul v-for="item in category.items" :key="item">
                                                    <li> {{ item }} </li>
                                                </ul>
                                            </li>
                                        </ul>
                                        </p>
                                    </div>
                                </div>
                                <br />
                            </div>
                        </div>
                               <div class="row mt-3">
                                <div class="col text-start">
                                    <button class="btn btn-primary" @click="showView(3)">
                                        <i class="fa-solid fa-chevron-left"></i> Anterior
                                    </button>
                                </div>
                                <div class="col text-end">
                                    <button class="btn btn-success" @click="showView(5)">
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
    emits: ['showView',],
    props: {
        taking_data: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            all_categories: [],
        }
    },
    methods: {
        showView(view) {
            this.$emit('showView', view);
        },showView(view) {
            this.$emit("showView", view);
        }
    },mounted() {
        
    },computed:{
        selected_categories(){
            return this.taking_data.categories.filter((item)=>{
                return item.selected;
            });
        }
    }
}
</script>