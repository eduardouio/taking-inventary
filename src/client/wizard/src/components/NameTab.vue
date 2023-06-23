<template>
    <div class="row mt-2">
        <h5 class="mt-2">NOMBRE DE LA TOMA</h5>
        <div class="col bg-light">
            <div class="row mt-3">
                <div class="col text-end">
                    <div class="card mt-5">
                        <div class="card-body text-start">
                            <h5 class="card-title text-info">Recomendación</h5>
                            <p class="card-text text-secondary">
                                Se recomienda el uso de nombre cortos, no importa si los nombres son los mismo en
                                cada toma, el sistema asigna un código único a cada toma.
                                <br />
                                <br />
                                Por ejemplo:
                            <ul class="list-group">
                                <li class="list-group-item text-secondary p-1">Guarda Cuenca</li>
                                <li class="list-group-item text-secondary p-1">Vinesa 10 De Agosto</li>
                                <li class="list-group-item text-secondary p-1">Vinlitoral Parque California</li>
                                <li class="list-group-item text-secondary p-1">Guarda Xima</li>
                                <li class="list-group-item text-secondary p-1">Sermultimarc</li>
                            </ul>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <input 
                    type="text" 
                    class="form-control" 
                    maxlength="30"
                    v-model="taking_name"
                    @blur="updateName"
                    autofocus>
                </div>
            </div>
            <div class="row mt-2">
                <div class="col text-end">
                    <button class="btn btn-success btn-sm" @click="showView(2)">
                        Siguiente <i class="fa-solid fa-chevron-right"></i>
                    </button>
                </div>
            </div>
            <br />
        </div>

    </div>
</template>
<script>
export default {
    name: 'NameTab',
    emits: ['updateName', 'showView'],
    props: {
        migration_data: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            taking_name: '',
        }
    },
    methods: {
        updateName() {
            this.taking_name = this.taking_name.toUpperCase();
            this.$emit('updateName', this.taking_name);
        },
        showView(view) {
            this.$emit('showView', view);
        }
    }
};
</script>