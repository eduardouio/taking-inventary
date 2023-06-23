<template>
    <div class="row mt-2">
        <h5 class="mt-2">ASISTENTES DE TOMA</h5>
        <div class="col bg-light">
            <div class="row">
                <div class="col-8 mt-2">
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
                            <tr>
                                <td>1</td>
                                <td>Juan Perez</td>
                                <td>jperez</td>
                                <td class="text-danger"><i class="fa-solid fa-minus"></i></td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>M Paula Villota</td>
                                <td>mvillota</td>
                                <td class="text-success"><i class="fa-solid fa-check"></i></td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td>Carlos Ponce</td>
                                <td>cponce</td>
                                <td class="text-danger"><i class="fa-solid fa-minus"></i></td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td>Fernanda Mazon</td>
                                <td>fmazon</td>
                                <td class="text-success"><i class="fa-solid fa-check"></i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-4 mt-2">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Usuarios Seleccionados</h5>
                            <p class="card-text">
                            <ul class="list-group text-start">
                                <li class="list-group-item p-1">M Paula Villota</li>
                                <li class="list-group-item p-1">Fernanda Mazon</li>
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
        migration_data: {
            type: Object,
            required: true,
        },
    },
};
</script>