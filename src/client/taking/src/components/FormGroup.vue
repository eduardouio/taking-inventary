<template>
    <div class="card card-outline card-secondary">
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
    					<input type="text" class="form-control" v-model="user.fields.username" readonly>
    				</div>
    			</div>
    			<div class="row">
    				<div class="col">
    					Asistente:
    					<input type="text" class="form-control" v-model="team.fields.warenhouse_assistant">
    				</div>
    			</div>
    			<div class="row">
    				<div class="col">
    					Notas:
    					<textarea cols="30" rows="2" class="form-control" v-model="team.fields.notes"></textarea>
    				</div>
    			</div>
    			<div class="row">
    				<div class="col">
    					<button class="btn btn-secondary btn-block" @click="changeView"> <i class="fas fa-users"> </i>
    						Confirmar Grupo</button>
    				</div>
    			</div>
    		</div>
    	</div>
</template>
<script>
export default {
    name: 'FormGroup',
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
	}
}
</script>
