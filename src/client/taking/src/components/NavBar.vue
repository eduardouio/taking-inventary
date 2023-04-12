<template>
    <div class="navBar">
        <div class="card card-outline card-primary">
            <div class="card-header">
                <div class="row">
                    <div class="col-8">
                        <button class="btn btn" @click="changeView('search_form')">
                            <i class="fas fa-search text-primary"></i>
                        </button>
                        &nbsp;
                        <button class="btn btn" @click="changeView('report_primary')">
                            <i class="fas fa-table text-primary"></i>
        <span class="visually-hidden">unread messages</span>
                            <small  class="badge rounded-pill bg-danger">{{ report.length }}</small>
                        </button>
                        &nbsp;
                        <button class="btn btn" @click="changeView('group_form')">
                            <i class="fas fa-users text-primary"></i>
                        </button>
                    </div>
                    <div class="col-4 text-rigth">
                        <button class="btn btn-sm bordered fw-bold" @click="showDetails">
                            Toma #{{ taking.pk }} 
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="row bordered" v-if="show_details">
            <div class="col-3 text-end">
                <strong class="text-secondary">Toma: </strong>
                    <br>
                    <strong class="text-secondary">Grupo: </strong>
                    <br>
                    <strong class="text-secondary">Nombre: </strong>
                    <br>
                    <strong class="text-secondary">Fecha: </strong>
                    <br>
                    <strong class="text-secondary">Asistente: </strong>
                    <br>
                    <strong class="text-secondary">Auxiliar: </strong>
                    <br>
                    <strong class="text-secondary">Token: </strong>
                    <br>
            </div>
            <div class="col text-break">
                 {{ taking.pk }}
                <br>
                 {{ team.fields.group_number }}
                <br>
                <span class="text-primary" v-text="taking.fields.name"></span>
                <br>
                <span v-text="new Date(taking.fields.created).toLocaleString('es-EC')"></span>
                <br>
                <span>{{ user.fields.first_name }} {{ user.fields.last_name }}</span>
                <br>
                <span v-text="team.fields.warenhouse_assistant"></span>
                <span v-text="team.fields.token_team"></span>
            </div>
            <button class="btn btn-block btn-dark text-center" @click="showDetails">
                <i class="fas fa-info-circle"></i>
                Cerrar
            </button>
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
    emits: ['changeView'],
    methods: {
        changeView(view) {
            this.$emit('changeView', view);
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