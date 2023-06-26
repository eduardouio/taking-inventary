<template>
    <div class="row mt-2">
        <h5 class="mt-2">ASISTENTES DE TOMA</h5>
        <div class="col bg-light">
            <div class="row">
                <div class="col-8 mt-2">
                    <input type="text" v-model="query" class="form-control" placeholder="Buscar">
                    <table class="table table-bordered table-hover table-condesed mi_table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Nombre</th>
                                <th>Username</th>
                                <th><i class="fas fa-cogs"></i></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(user, idx) in all_teams" :key="user" @click="selectUser(user)">
                                <td class="text-center">{{ idx+1 }}</td>
                                <td class="text-start">{{ user.last_name }} {{ user.first_name }}</td>
                                <td class="text-start">{{ user.username }}</td>
                                <td class="text-success"><i class="fa-solid fa-plus"></i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-4 mt-2">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Usuarios Seleccionados</h5>
                            <p class="card-text">
                            <ul class="list-group text-start" v-for="user in selected_teams" :key="user">
                                <li class="list-group-item p-1" @click="selectUser(user,true)">
                                    <li class="fa-solid fa-minus text-danger"></li>
                                    {{ user.last_name }} {{ user.first_name }}
                                    <small class="badge bg-light text-secondary border">{{ user.username }}</small>
                                </li>
                            </ul>
                            </p>
                        </div>
                    </div>
                    <br />
                </div>
            </div>
            <div class="row mt-3">
                <div class="col text-start">
                    <button class="btn btn-primary btn-sm" @click="showView(2)">
                        <i class="fa-solid fa-chevron-left"></i> Anterior
                    </button>
                </div>
                <div class="col text-end">
                    <button class="btn btn-success btn-sm" @click="showView(4)">
                        Siguiente<i class="fa-solid fa-chevron-right"></i>
                    </button>
                </div>
            </div>
            <br />
        </div>
    </div>
</template>
<script>
export default {
    name: "TeamsTab",
    emits: ["updateTeams"],
    props: {
        teams: {
            type: Object,
            required: true,
        },
    },data(){
        return{
            query:"",
            all_teams: [],
            selected_teams: [],
        }
    },methods:{
        filterUsers(){
            // tomamos todos los usuarios
            const users = this.all_teams.map(item=>item);

            // quitamos los seleccionados
          this.all_teams = users.filter(
            item=>!this.selected_teams.includes(item)
         );

         // aplicamos el filtro
         if (this.query.length > 0){
             this.all_teams = this.all_teams.filter(
                 item=>item.username.includes(this.query)
             );
             return;
         }

        },
        selectUser(user, delete_usr=false){
            // agregamos un usuario a los seleccionados
            if (delete_usr){
                this.selected_teams = this.selected_teams.filter(
                    item=>item.username !== user.username
                );
                return;
            }
            this.selected_teams.push(user);
            this.filterUsers();
        },
    },
    mounted(){
        // cargar todos los usuarios asistentes
        this.all_teams = this.teams.map(item=>item);
    },
};
</script>