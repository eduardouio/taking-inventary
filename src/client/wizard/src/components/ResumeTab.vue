<template>
    <div class="row mt-1">
        <h5 class="mt-1">RESUMEN DE TOMA</h5>
        <div class="alert alert-danger p-1" role="alert" v-if="!isValidData">
          <h6>Informacion incompleta, por favor verifíque todos los campos para continuar</h6>
    </div>
        <div class="col bg-light">
            <div class="row">
                <div class="col">
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Nombre Toma:</strong></div>
                        <div class="col text-start">
                            <ul class="list-group text-start">
                                <li class="list-group-item p-1">{{ taking_data.name }}</li>
                            </ul>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Bodegas Seleccionadas:</strong></div>
                        <div class="col">
                            <ul class="list-group text-start" v-for="warenhouse in taking_data.warenhouses" :key="warenhouse">
                                <li class="list-group-item p-1">{{ warenhouse.warenhouse }}</li>
                            </ul>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Grupos Asignados:</strong></div>
                        <div class="col">
                            <ul class="list-group text-start" v-for="user in taking_data.groups" :key="user.username">
                                <li class="list-group-item p-1"> 
                                    <small class="bage bg-light border">{{ user.username }}</small> 
                                    &nbsp;
                                    {{ user.first_name }} {{ user.last_name }} 
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Items a Contar:</strong></div>
                        <div class="col">
                            <ul class="list-group text-start" v-for="category in taking_data.categories.filter(item=>item.selected)" :key="category.category">
                                <li class="list-group-item p-1">{{ category.category }}</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col text-start">
                    <button class="btn btn-primary" @click="showView(4)">
                        <i class="fa-solid fa-chevron-left"></i> Anterior
                    </button>
                </div>
                <div class="col text-end">
                    <button class="btn btn-success" v-if="isValidData" @click="sendData">
                        Finalizar <i class="fa-solid fa-chevron-right"></i>
                    </button>
                </div>
            </div>
            <br />
        </div>
    </div>
</template>
<script>
export default {
    name: "ResumeTab",
    emits: ["showView", 'sendData'],
    props: {
        taking_data: {
            type: Object,
            required: true
        }
    },methods: {
        showView(view) {
            this.$emit("showView", view);
        },sendData() {
            this.$emit("sendData");
        }
    }, computed:{
        isValidData(){
            return this.taking_data.name != "" && this.taking_data.warenhouses.length > 0 && this.taking_data.groups.length > 0 && this.taking_data.categories.length > 0;
        }
    },
};
</script>