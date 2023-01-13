app.component('form-group', {
    template:`
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
					<input type="text" class="form-control" value="{{ request.user }}" readonly>
				</div>
			</div>
			<div class="row">
				<div class="col">
					Asistente:
					<input type="text" class="form-control" model="team.fields.warenhouse_assistant">
				</div>
			</div>
			<div class="row">
				<div class="col">
					Notas:
					<textarea cols="30" rows="2" class="form-control" model="team.fields.notes"></textarea>
				</div>
			</div>
			<div class="row">
				<div class="col">
					<button class="btn btn-secondary btn-block" @click="registerTeam"> <i class="fas fa-users"> </i>
						Confirmar Grupo</button>
				</div>
			</div>
		</div>
	</div>`,
    data(){
        
    },methods:{
        registerTeam(){
        this.have_team = true;
        const formData = new FormData()
        formData.append('team', JSON.stringify(this.team));
        let xhr = new XMLHttpRequest
        xhr.open(
            'POST',
            '/accounts/team/update/'
        );
        xhr.setRequestHeader('X-CSRFToken', this.csrftoken);
        xhr.onreadystatechange = function() {
            console.log(xhr);
        }
        xhr.onerror = function(e){
            alert("No es posible comunicarse con el servidor, confirme su conección a la red");
        }

        xhr.send(formData); 
        xhr.onload = ()=>{
            if(xhr.status == 200){
                this.have_team = true;
                return xhr.responseText;
            }
            this.show_error = true;
            console.dir(xhr.responseText);
            return xhr.responseText;
        }
    }
    },
});