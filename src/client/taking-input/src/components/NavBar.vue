<template>
    <div class="navBar">
        <div class="card card-outline card-primary">
            <div class="card-header">
                <div class="row">
                    <div class="col-9">
                        <button class="btn btn" @click="switchView('search_form')">
                            <i class="fas fa-search text-primary"></i>
                        </button>
                        &nbsp;
                        <button class="btn btn" @click="switchView('report_info')">
                            <i class="fas fa-table text-primary"></i>
        <span class="visually-hidden">unread messages</span>
                            <small  class="badge rounded-pill bg-danger">{{ report.length }}</small>
                        </button>
                        &nbsp;
                        <button class="btn btn" @click="switchView('group_form')">
                            <i class="fas fa-users text-primary"></i>
                        </button>
                        &nbsp;
                        <small class="badge bg-secondary" @click="switchView('taking_form')">
                            T #{{ taking.id_taking  }}
                        </small>
                    </div>
                    <div class="col-3 text-end">
                        <button class="btn btn-sm bordered fw-bold" @click="showDetails">
                            <i class="fas fa-info-circle text-primary"></i> Toma: {{ taking.pk }} 
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="show_details">
        <div class="row bordered">
            <div class="col">
                <div class="row">
                    <div class="col-3 text-end border">
                        <strong class="text-secondary">Toma: </strong>
                    </div>
                    <div class="col border">
                       {{ taking.id_taking }}
                    </div>
                </div>
                <div class="row">
                    <div class="col-3 text-end border">
                        <strong class="text-secondary">Grupo: </strong>
                    </div>
                    <div class="col border">
                        Grupo Nro {{ team.group_number }}
                        | <smal class="badge bg-secondary">#{{ team.id_team }}</smal>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3 text-end border">
                        <strong class="text-secondary">Nombre: </strong>
                    </div>
                    <div class="col border">
                       <span class="text-primary" v-text="taking.name"></span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3 text-end border">
                        <strong class="text-secondary">Fecha: </strong>
                    </div>
                    <div class="col border">
                        <span v-text="new Date(taking.created).toLocaleString('es-EC')"></span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3 text-end border">
                        <strong class="text-secondary">Asistente: </strong>
                    </div>
                    <div class="col border">
                        <span>{{ user.first_name }} {{ user.last_name }}</span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3 text-end border">
                         <strong class="text-secondary">Auxiliar: </strong>
                    </div>
                    <div class="col border">
                        <span>{{ team.warenhouse_assistant }}</span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3 text-end border">
                        <strong class="text-secondary">Token: </strong>
                    </div>
                    <div class="col text-break border">
                        <span v-text="team.token_team"></span>
                    </div>
                </div>
            </div>
            </div>
            <div class="row">
            <button class="btn btn-block btn-dark text-center" @click="showDetails">
                <i class="fas fa-info-circle"></i>
                Cerrar
            </button>
        </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'NavBar',
    props: {
        taking: {
            type: Object,
            default: null,
            required: true,
        },
        team: {
            type: Object,
            default: null,
            required: true,
        },
        user: {
            type: Object,
            default: null,
            required: true,
        },
        report: {
            type: Array,
            default: null,
            required: true,
        },
    },
    data() {
        return {
            show_details: false,
        }
    },
    emits: ['switchView'],
    methods: {
        switchView(view) {
            this.$emit('switchView', view);
        },showDetails() {
            this.show_details = !this.show_details;
        }
    }
}
</script>
<style>
.navBar {
    padding-top: 0.35rem;
}
.card-header {
    padding: 0.12rem 0.15rem;
    padding-left: 0.15rem;
    margin-bottom: 0;
    background-color: rgba(0, 0, 0, 0.03);
    border-bottom: 0 solid rgba(0, 0, 0, 0.125);
}
</style>