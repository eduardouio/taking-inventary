app.component('status-message', {
    template: /* vue-html */`
    <div class="card card-outline card-primary">
        <div class="card-header">
            <div class="row">
                <strong class="text-info" v-text="[taking.pk]"></strong>
                <div class="col">
                    <strong>Fecha:</strong> 
                    <span 
                        v-text="new Date(taking.fields.created).toLocaleString('es-EC')">
                    </span>
                </div>
                <div class="col-2 text-center">
                    <button
                        class="btn bordered btn"
                        @click="changeView()">
                        <i class="fas fa-home text-info"></i>
                    </button>
                </div>
            </div>
            <div class="row" v-if="$parent.server_status.have_error_message">
                <div class="col text-center">
                    <div class="alert alert-danger" role="alert">
                        <i class="fas fa-exclamation-triangle"></i>
                        Error al comunicarse con el Serivor
                    </div>
                </div>
            </div>
            <div class="row" v-if="$parent.server_status.have_warning_message">
                <div class="col text-center">
                    <div class="alert alert-warning" role="alert">
                        <i class="fas fa-exclamation-circle"></i>
                        Tiene datos sin Sincronizar
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <strong>Grupo: [#<span v-text="team.fields.group_number"></span> ]</strong>
                    <span>{{user.fields.first_name}} {{user.fields.last_name}} </span>
                    |
                    <span v-text="team.fields.warenhouse_assistant"></span>
                </div>
            </div>
        </div>
    </div>
    `,
    props:['taking', 'team', 'user',],
    emits: ['changeview',],
    data() { 
        return{};
    },methods:{
        changeView(){
            this.$emit('changeview', 'search_form');
        }
    }
});