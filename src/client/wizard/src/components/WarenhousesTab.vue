<template>
    <div class="row mt-2">
        <h5 class="mt-2">BODEGAS DISPONIBLES</h5>
        <div class="col bg-light">
            <div class="row">
                <div class="col">
                    <div class="row">
                        <div class="col-8 mt-2">
                            <div class="input-group input-group-sm mb-3">
                                <span class="input-group-text" id="inputGroup-sizing-sm">Filtrar: </span>
                                <input type="text" 
                                    class="form-control" 
                                    aria-label="Sizing example input"
                                    aria-describedby="inputGroup-sizing-sm"
                                    v-model="filter_query"
                                    @keyup="filterWarenhouses"
                                    >
                            </div>
                            <table class="table table-bordered table-hover mi_table">
                                <thead>
                                    <tr>
                                        <th>#</th>
                                        <th>Bodega</th>
                                        <th><i class="fas fa-cogs"></i></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(warenhouse, idx) in all_warenhouses.filter(item => !item.selected)" :key="warenhouse" @click="updateWarenhouse(warenhouse)">
                                        <td>{{ idx + 1 }}</td>
                                        <td class="text-start">{{ warenhouse.warenhouse }}</td>
                                        <td class="text-center">
                                            <i class="fa-solid fa-plus text-success"></i>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="col-4">
                                <div class="card-body border-blue">
                                    <h6 class="card-title bg-secondary-light">Bodegas Seleccionadas</h6>
                                    <ul class="list-group text-start" v-for="warenhouse in taking_data.warenhouses"
                                        :key="warenhouse">
                                        <li class="list-group-item p-1" @click="updateWarenhouse(warenhouse, true)">
                                            <i class="fa-solid fa-minus text-danger"></i>
                                            &nbsp;
                                            {{ warenhouse.warenhouse }}
                                        </li>
                                    </ul>
                            </div>
                            <br/>
                                <div class="card-body border-blue">
                                    <h6 class="card-title bg-secondary-light">Propietarios</h6>
                                    <ul class="list-group text-start" v-for="owner in warehouses_owner" :key="owner">
                                        <li class="list-group-item p-1">{{ owner }}</li> 
                                    </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col text-start">
                    <button class="btn btn-primary" @click="showView(1)">
                        <i class="fa-solid fa-chevron-left"></i> Anterior
                    </button>
                </div>
                <div class="col text-end">
                    <button class="btn btn-success" @click="showView(3)">
                        Siguiente<i class="fa-solid fa-chevron-right"></i>
                    </button>
                </div>
            </div>
            <br />
        </div>

    </div>
</template>
<script>
export default {
    name: "WarenhousesTab",
    emits: ["showView"],
    props: {
        migration_data: {
            type: Object,
            required: true,
        }, taking_data: {
            type: Object,
            required: true
        }
    },data(){
        return {
            all_warenhouses: [],
            owners: [],
            filter_query: "",
            warehouses_owner: [],
        }
    },
    mounted(){
        // cargamos la lista de las bodegas
        this.all_warenhouses = this.migration_data.warenhouses.map(item => {
            return {
                warenhouse: item,
                selected: false,
            };
        });
        this.updateOwners();
    },
    methods: {
        filterWarenhouses() {
            // tomamos todas las bodegas
            this.all_warenhouses = this.migration_data.warenhouses.map(item => {
                return {
                    warenhouse: item,
                    selected: false,
                };
            });

            // qutiando los que ya estan seleccionados
            this.all_warenhouses = this.all_warenhouses.filter(item => {
                return !this.taking_data.warenhouses.some(warenhouse => {
                    return warenhouse.warenhouse === item.warenhouse;
                });
            });

            // aplicando el filtro
            if (this.filter_query.length > 3) {
                this.all_warenhouses = this.all_warenhouses.filter(item => {
                    return item.warenhouse.toLowerCase().includes(this.filter_query.toLowerCase());
                });
                return;
            }
        },
        showView(view) {
            this.$emit("showView", view);
        },
        updateWarenhouse(warenhouse, delete_warenhouse = false) {
            // quitamos una bodega de la lista de seleccionadas
            if (delete_warenhouse){
                this.taking_data.warenhouses = this.taking_data.warenhouses.filter(item => {
                    return item.warenhouse !== warenhouse.warenhouse;
                });
                this.filterWarenhouses();
                this.updateOwners();
                return;
            }
            // agregar bodegas a la lista de seleccionadas
            warenhouse.selected = true;
            this.taking_data.warenhouses.push(warenhouse);
            this.updateOwners();
        },
        updateOwners(){
            this.warehouses_owner = [];
            // listamos todas las bodegas y sus propietarios
           const all_owners = this.migration_data.warenhouses_owners.map(
                item=>item
            );
            
            all_owners.filter((item)=>{
                this.taking_data.warenhouses.some((warenhouse)=>{
                    if (warenhouse.warenhouse === item.warenhouse_name){
                        this.warehouses_owner.push(item.owners.map(item=>item));
                    }
                });
            }
            );
            // quitamos los repetidos
            this.warehouses_owner = this.warehouses_owner.flat();
            this.warehouses_owner = [...new Set(this.warehouses_owner)];
        },
    },
};
</script>