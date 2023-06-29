<template>
    <div class="row mt-2">
        <h5 class="mt-2">ASISTENTES DE TOMA</h5>
        <div class="col bg-light">
            <div class="row">
                <div class="col-8 mt-2">
                    <input type="text" v-model="query" class="form-control" placeholder="Buscar" @keyup="filterUsers">
                    <table class="table table-bordered table-hover table-condensed mi_table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Nombre</th>
                                <th>Username</th>
                                <th><i class="fas fa-cogs"></i></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(user, idx) in all_teams" :key="user.id" @click="updateTeams(user)">
                                <td class="text-center">{{ idx+1 }}</td>
                                <td class="text-start">{{ user.last_name }} {{ user.first_name }}</td>
                                <td class="text-start">{{ user.username }}</td>
                                <td class="text-success"><i class="fa-solid fa-plus"></i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-4">
                        <div class="card-body bg-secondary-light border-blue">
                            <h6 class="card-title">Usuarios Seleccionados</h6>
                            <ul class="list-group text-start" v-for="user in taking_data.groups" :key="user.username" @click="updateTeams(user,true)">
                                <li class="list-group-item p-1">
                                    <i class="fa-solid fa-minus text-danger"></i>
                                    {{ user.last_name }} {{ user.first_name }}
                                    <small class="badge bg-light text-secondary border">{{ user.username }}</small>
                                </li>
                            </ul>
                    </div>
                    <br />
                </div>
            </div>
            <div class="row mt-3">
                <div class="col text-start">
                    <button class="btn btn-primary" @click="showView(2)">
                        <i class="fa-solid fa-chevron-left"></i> Anterior
                    </button>
                </div>
                <div class="col text-end">
                    <button class="btn btn-success" @click="showView(4)">
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
    emits: ["showView"],
    props: {
        teams: {
            type: Object,
            required: true,
        },taking_data: {
            type: Object,
            required: true,
        },
    },data(){
        return{
            query:"",
            all_teams: [],
        }
    },methods:{
        filterUsers(){
        // tomamos todos los usuarios
        this.all_teams = this.teams.map(item=>item);

        // quitamos los seleccionados
       this.all_teams = this.all_teams.filter(item=>{
            return !this.taking_data.groups.some(item2=>item2.username == item.username);
        });

        // filtramos por el query
        this.all_teams = this.all_teams.filter(item=>{
            return item.username.toLowerCase().includes(this.query.toLowerCase()) || 
            item.first_name.toLowerCase().includes(this.query.toLowerCase()) || 
            item.last_name.toLowerCase().includes(this.query.toLowerCase());
        });
        },showView(view) {
            this.$emit("showView", view);
        }, updateTeams(user, delete_user = false){
            if(delete_user){
                this.taking_data.groups = this.taking_data.groups.filter(item=>item.username != user.username);
            }else{
                this.taking_data.groups.push(user);
            }
            this.filterUsers();
        },
    },
    mounted(){
        // cargar todos los usuarios asistentes
        this.filterUsers();
    },computed(){
    }
};
</script>