<template>
    <div class="card card-outline card-secondary mt-1">
    		<div class="card-header">
    			<div class="row ">
    				<div class="col text-center">
    					<i class="fas fa-users"></i>
    					<strong>
    						Información de Grupo
    					</strong>
    				</div>
    			</div>
    			<div class="row">
    				<div class="col">
    					Manager:
    					<input type="text" class="form-control" :value="user.first_name + ' ' + user.last_name" readonly>
    				</div>
    			</div>
    			<div class="row">
    				<div class="col">
    					Asistente:
    					<input type="text" class="form-control" v-model="team.warenhouse_assistant">
    				</div>
    			</div>
    			<div class="row">
    				<div class="col">
    					Notas:
    					<textarea cols="30" rows="2" class="form-control" v-model="team.notes"></textarea>
    				</div>
    			</div>
    			<div class="row mt-1">
    					<button 
							class="btn btn-primary btn-block" 
							@click="updateTeam"> 
							<i class="fas fa-users"> </i>Confirmar Grupo</button>
    			</div>
    		</div>
    	</div>
</template>
<script>
import appConfig from ".././appConfig";

export default {
    name: 'FormGroup',
	emits: ['switchView'],
    props: {
		team: {
			type: Object,
			default: null,
			required: true,
		},user:{
			type: Object,
			default: null,
			required: true,
		}, show_view: {
			type: Object,
			default: null,
			required: true,
		},server_status: {
			type: Object,
			default: null,
			required: true,
		},have_team: {
			type: Boolean,
			default: false,
			required: true,
		},
	},
	methods: {
		switchView(viewName){
			console.log('emitimos el evento switchView');
			this.$emit('switchView', viewName);
		},updateTeam() {
		this.show_view.loader = true;
		this.server_status.response = null;
		this.server_status.message = null;

		fetch(appConfig.updateTeamURL, {
			method: 'PUT',
			headers:appConfig['headers'],
			body: JSON.stringify(this.team),
		}).then(response => {
			if (response.status === 200) {
			this.server_status.issue_type = 'success';
			this.server_status.message = 'Completado correctamente';
			this.server_status.response = response.responseText;
			console.log(`emitimos el evento switchView ${this.have_team}`);
			this.switchView('search_form');
			} else {
			this.server_status.issue_type = 'error';
			this.server_status.message = `Servidor Desconectado ${response.responseText}`;
			this.switchView('group_form');
			}
		}).catch(error => {
			this.show_view.loader = false;
			this.server_status.issue_type = 'error';
			this.server_status.message = 'Error al cargar los datos -> ${error}';
			this.switchView('group_form');
		});
		},
	}
}
</script>
