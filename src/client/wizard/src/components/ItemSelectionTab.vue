<template>
    <div class="row mt-2">
                    <h5 class="mt-2">PERSONALIZAR ITEMS TOMA</h5>
                    <div class="col bg-light">
                        <div class="row">
                            <div class="col-8 mt-2">
                                <table class="table table-bordered table-hover table-condesed mi_table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Tipo</th>
                                            <th><i class="fas fa-cogs"></i></th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>1</td>
                                            <td>Accesorios</td>
                                            <td class="text-danger"><i class="fa-solid fa-minus"></i></td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                            <td>Licores</td>
                                            <td class="text-success"><i class="fa-solid fa-check"></i></td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                            <td>Alimentos</td>
                                            <td class="text-success"><i class="fa-solid fa-check"></i></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="col-4 mt-2">
                                <div class="card">
                                    <div class="card-body">
                                        <h5 class="card-title">Items Seleccionados</h5>
                                        <p class="card-text">
                                        <ul class="list-group text-start">
                                            <li class="list-group-item p-1">Licores</li>
                                            <li class="list-group-item p-1">Alimentos</li>
                                        </ul>
                                        </p>
                                    </div>
                                </div>
                                <br />
                            </div>
                        </div>
                               <div class="row mt-3">
                                <div class="col text-start">
                                    <button class="btn btn-primary btn-sm" @click="showView(3)">
                                        <i class="fa-solid fa-chevron-left"></i> Anterior
                                    </button>
                                </div>
                                <div class="col text-end">
                                    <button class="btn btn-success btn-sm" @click="showView(5)">
                                        Siguiente<i class="fa-solid fa-chevron-right"></i>
                                    </button>
                            </div>
                            </div>
                            <br/>
                    </div>

                </div>
</template>

<script>
export default {
    name: 'ItemSelectionTab',
    methods: {
        showView(view) {
            this.$emit('showView', view);
        }
    }
}

</script>