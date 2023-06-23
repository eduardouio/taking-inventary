<template>
    <div class="row mt-2">
        <h5 class="mt-2">BODEGAS DISPONIBLES</h5>
        <div class="col bg-light">
            <div class="row">
                <div class="col">
                    <div class="row">
                        <div class="col-8 mt-2">
                            <div class="input-group input-group-sm mb-3">
                                <span class="input-group-text" id="inputGroup-sizing-sm">Filtrar: </span>
                                <input type="text" class="form-control" aria-label="Sizing example input"
                                    aria-describedby="inputGroup-sizing-sm">
                            </div>
                            <table class="table table-bordered table-hover mi_table">
                                <thead>
                                    <tr>
                                        <th>#</th>
                                        <th>Bodega</th>
                                        <th><i class="fas fa-cogs"></i></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(whrs, idx) in warenhouses" :key="whrs" @click="updateWarenhousesList(whrs)">
                                        <td>{{ idx + 1 }}</td>
                                        <td class="text-start">{{ whrs.warenhouse }}</td>
                                        <td class="text-center">
                                            <i class="fa-solid fa-check text-success" v-if="whrs.selected"></i>
                                            <i class="fa-solid fa-minus text-danger" v-else></i>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="col-4 mt-2">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title text-info">Bodegas Seleccionadas</h5>
                                    <p class="card-text">
                                    <ul class="list-group text-start" v-for="whrs_sel in warenhouses_selected"
                                        :key="whrs_sel">
                                        <li class="list-group-item p-1">{{ whrs_sel.warenhouse }}</li>
                                    </ul>
                                    </p>
                                </div>
                            </div>
                            <hr>
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title text-info">Propietarios</h5>
                                    <p class="card-text">
                                    <ul class="list-group text-start">
                                        <li class="list-group-item p-1">VINESA</li>
                                        <li class="list-group-item p-1">VINESA</li>
                                        <li class="list-group-item p-1">VINESA</li>
                                    </ul>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col text-start">
                    <button class="btn btn-primary btn-sm" @click="showView(1)">
                        <i class="fa-solid fa-chevron-left"></i> Anterior
                    </button>
                </div>
                <div class="col text-end">
                    <button class="btn btn-success btn-sm" @click="showView(3)">
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
    name: "WarenhousesTab",
    props: {
        warenhouses: {
            type: Array,
            required: true,
        },
        warenhouses_selected: {
            type: Array,
            required: true,
        },
    },
    methods: {
        updateWarenhousesList(whrs) {
            this.$emit("updateWarenhousesList", whrs);
        },
        showView(view) {
            this.$emit("showView", view);
        },
    },
};
</script>