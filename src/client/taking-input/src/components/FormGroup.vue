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
							@click="updateGroup"> 
							<i class="fas fa-users"> </i>Confirmar Grupo</button>
    			</div>
    		</div>
    	</div>
</template>
<script>
export default {
    name: 'FormGroup',
	emits: ['updateGroup'],
    props: {
		team: {
			type: Object,
			default: null,
			required: true,
		},
		user:{
			type: Object,
			default: null,
			required: true,
		}
	},
	methods: {
		updateGroup(){
			this.$emit('updateGroup', this.team)
		},
	}
}
</script>
