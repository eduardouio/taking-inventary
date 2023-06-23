<template>
    <div class="row mt-2">
        <h5 class="mt-2">RESUMEN DE TOMA</h5>
        <div class="col bg-light">
            <div class="row">
                <div class="col">
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Nombre Toma:</strong></div>
                        <div class="col text-start">
                            <ul class="list-group text-start">
                                <li class="list-group-item p-1">Guarda Cuenca</li>
                            </ul>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Bodegas Seleccionadas:</strong></div>
                        <div class="col">
                            <ul class="list-group text-start">
                                <li class="list-group-item p-1">Guarda Cuenca</li>
                                <li class="list-group-item p-1">Vinesa 10 De Agosto</li>
                                <li class="list-group-item p-1">Vinlitoral Parque California</li>
                                <li class="list-group-item p-1">Guarda Xima</li>
                                <li class="list-group-item p-1">Sermultimarc</li>
                            </ul>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Grupos Asignados:</strong></div>
                        <div class="col">
                            <ul class="list-group text-start">
                                <li class="list-group-item p-1">Juan Pardo</li>
                                <li class="list-group-item p-1">Estaban Sigcha</li>
                                <li class="list-group-item p-1">Juan Pablo</li>
                                <li class="list-group-item p-1">Marco Guamani</li>
                                <li class="list-group-item p-1">Leonardo Pancgi</li>
                            </ul>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col text-end"><strong>Items a Contar:</strong></div>
                        <div class="col">
                            <ul class="list-group text-start">
                                <li class="list-group-item p-1">Licores</li>
                                <li class="list-group-item p-1">Accesorios</li>
                                <li class="list-group-item p-1">Varios</li>
                                <li class="list-group-item p-1">Alimentos</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col text-start">
                    <button class="btn btn-primary btn-sm" @click="showView(4)">
                        <i class="fa-solid fa-chevron-left"></i> Anterior
                    </button>
                </div>
                <div class="col text-end">
                    <button class="btn btn-success btn-sm">
                        Finalizar <i class="fa-solid fa-chevron-right"></i>
                    </button>
                </div>
            </div>
            <br />
        </div>
    </div>
</template>
<script>
export default {
    name: "ResumeTab",
    props: {
        migration_data: {
            type: Object,
            default: null
        }
    },
};
</script>