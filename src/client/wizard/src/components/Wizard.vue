<template>
    <div class="container text-center">
        <div class="row shadow-sm">
            <ul class="nav nav-pills nav-fill">
                <li class="nav-item" @click="showView(1)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step1 }">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-home"></i>
                        </span>
                        &nbsp;
                        Nombre
                    </a>
                </li>
                <li class="nav-item" @click="showView(2)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step2 }">
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
                :taking_data="taking_data"
                @showView="showView($event)"
                @updateName="updateName($event)">
            </name-tab>
            <!--/Paso 1-->
            <!--Paso 2-->
            <warenhouses-tab 
                v-if="show_views.step2"
                :migration_data="migration_data"
                :taking_data="taking_data"
                @showView="showView($event)"
                >
            </warenhouses-tab>
            <!--/Paso 2-->
            <!--Paso 3-->
            <teams-tab 
                v-if="show_views.step3"
                :teams="migration_data.all_users"
                :taking_data="taking_data"
                @showView="showView($event)"
                >
            </teams-tab>
            <!--/Paso 3-->
            <!--Paso 4-->
            <item-selection-tab 
                v-if="show_views.step4"
                :taking_data="taking_data"
                @showView="showView($event)">
            </item-selection-tab>
            <!--/Paso 4-->
            <!--Paso 5-->
            <resume-tab 
                v-if="show_views.step5"
                :taking_data="taking_data"
                :migration_data="migration_data"
                @showView="showView($event)"
                @sendData="sendData($event)"
                >
            </resume-tab>
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
    emits: ['updateName', 'sendData'],
    props: {
        migration_data: {
            type: Object,
            default: null
        },
    },
    data() { return {
        show_views : {
            step1 : true,
            step2 : false,
            step3 : false,
            step4 : false,
            step5 : false,
        },
        taking_data: {
           id_sap_migration: null,
           name: '',
           warenhouses: [],
           groups: [],
           categories: [],
        },
    }},methods: {
        showView(step){
            // seteamos todo en false
            this.show_views.step1 = false;
            this.show_views.step2 = false;
            this.show_views.step3 = false;
            this.show_views.step4 = false;
            this.show_views.step5 = false;
            // seteamos el paso que queremos mostrar
            let stepName = 'step'+step;
            this.show_views[stepName] = true;
        }, updateName( taking_name){
            // actualizamos el nombre de la toma
            this.taking_data.name = taking_name;
            this.$emit('updateName', taking_name);
        }, sendData(){
            // enviamos los datos
            this.$emit('sendData', this.taking_data);
        },//nextmethod
    },mounted(){
        // asignamos el id de la migracion
        this.taking_data.id_sap_migration = this.migration_data.sap_migration.id_sap_migration;
        // creamos la cateforias
        let all_categories = this.migration_data.type_products.map((item)=>{
            return item.type_product.split(";")[0];
        });
        all_categories = [...new Set(all_categories)];

        this.taking_data.categories = all_categories.map((item)=>{
            
            let items = this.migration_data.type_products.filter((category) => {
                return category.type_product.split(";")[0] == item;
            });

            items = items.map((item) => {
                return item.type_product.split(";")[1]
            });

            return {
                category: item,
                items: items,
                selected: false,
            }
        });
    }, //netx vuejs properties
};
</script>
<style>
/** table condensed with padding 0 */
.table> :not(caption)>*>* {
    padding: 0.15rem;
}
</style>