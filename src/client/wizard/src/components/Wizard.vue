<template>
    <div class="container text-center">
        <div class="row mt-2 shadow-sm">
            <ul class="nav nav-pills nav-fill">
                <li class="nav-item" @click="showView(1)">
                    <a class="nav-link" href="#" :class="{'active':show_views.step1}">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-home"></i>
                        </span>
                        &nbsp;
                        Nombre
                    </a>
                </li>
                <li class="nav-item" @click="showView(2)">
                    <a class="nav-link" href="#" :class="{'active': show_views.step2}">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-warehouse"></i>
                        </span>
                        &nbsp;
                        Bodegas
                    </a>
                </li>
                <li class="nav-item" @click="showView(3)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step3 }">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-users"></i>
                        </span>
                        &nbsp;
                        Grupos
                    </a>
                </li>
                <li class="nav-item" @click="showView(4)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step4 }">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-list-check"></i>
                        </span>
                        &nbsp;
                        Items
                    </a>
                </li>
                <li class="nav-item" @click="showView(5)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step5 }">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-chevron-down"></i>
                        </span>
                        Resumen
                    </a>
                </li>
            </ul>
        </div>
        <div class="row rounded border mt-2 shadow">
            <!--Paso 1-->
                <name-tab
                    v-if="show_views.step1"
                    :migration_data="migration_data"
                    @updateName="updateName">
                </name-tab>
            <!--/Paso 1-->
            <!--Paso 2-->
           <warenhouses-tab
                v-if="show_views.step2"
                :migration_data="migration_data"
                @updateWarehouses="updateWarehouses">
            </warenhouses-tab>
            <!--/Paso 2-->
            <!--Paso 3-->
            <teams-tab
                v-if="show_views.step3"
                :migration_data="migration_data"
            >
            </teams-tab>
            <!--/Paso 3-->
            <!--Paso 4-->
            <item-selection-tab
                v-if="show_views.step4"
                :migration_data="migration_data"
            >
            </item-selection-tab>
            <!--/Paso 4-->
            <!--Paso 5-->
            <resume-tab
                v-if="show_views.step5"
                :migration_data="migration_data"
           ></resume-tab>
            <!--/Paso 4-->

            <p></p> 
        </div>
    </div>
</template>
<script>
import NameTab from './NameTab.vue';
import WarenhousesTab from './WarenhousesTab.vue';
import TeamsTab from './TeamsTab.vue';
import ItemSelectionTab from './ItemSelectionTab.vue';
import ResumeTab from './ResumeTab.vue';

export default {
  components: { NameTab , WarenhousesTab, TeamsTab, ItemSelectionTab, ResumeTab},
    name: 'Wizard',
    emits: ['updateName','updateWarenhousesList'],
    data() { return {
        show_views : {
            step1 : true,
            step2 : false,
            step3 : false,
            step4 : false,
            step5 : false,
        },
        taking: {
           name: '',
           description: '',
           warehouses: [],
           groups: [],
           type_products: [],
        },
        warenhouses_selected: [],
        warenhouses: [],
    }},
    props: {
       migration_data: {
           type: Object,
           default: null
       }
    }, methods: {
        showView(step){
            // seteamos todo en false
            for (const key in this.show_views) {
                this.show_views[key] = false;
            }
            let stepName = 'step'+step;
            this.show_views[stepName] = true;
        }, updateName(){
            this.taking.name = this.taking.name.toUpperCase();
            console.log("Primer llamado a u[date]")
            this.$emit('updateName', this.taking.name);
        },updateWarenhousesList(warenhouse=false){
            // actualizamos las listas de bodegas, para mostrar
            // las seleccionadas y las no seleccionadas
           if(warenhouse){
            console.log('Actualizamos el estado de una bodega');
            this.$emit('updateWarenhousesList', warenhouse.warenhouse);
           }

            this.warenhouses = this.migration_data.warenhouses.map(item=>item);
            this.warenhouses_selected = this.migration_data.warenhouses.filter(
                (item) => {
                    if (item.selected) {
                         return true;
                    }
                }
            );

        }//nextmethod
    },mounted(){
        this.updateWarenhousesList();
    }, //netx vuejs properties
};
</script>
<style>
/** table condensed with padding 0 */
.table> :not(caption)>*>* {
    padding: 0.15rem;
}
</style>