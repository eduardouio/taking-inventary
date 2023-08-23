<template>
    <div class="row mt-3">
        <div class="col bg-light">
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body text-start">
                            <h5 class="card-title text-info">Recomendación</h5>
                            <p class="card-text text-secondary">
                                Se recomienda el uso de nombre cortos, no importa si los nombres son los mismo en
                                cada toma, el sistema asigna un código único a cada toma.
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
                    <div class="row mt-1">
                        <div class="input-group mb-1">
                            <div class="input-group mb-1">
                                <span class="input-group-text">Nombre de Toma</span>
                                <input type="text" class="form-control form-control-sm" maxlength="30" v-model="taking_name"
                                @blur="updateName('name')" autofocus>
                            </div>
                        </div>
                        <div class="col">
                            <div class="input-group mb-3">
                            <label class="input-group-text" for="inputGroupSelect01">Ubicación Toma &nbsp;</label>
                            <select class="form-select" id="inputGroupSelect01" v-model="location" @change="updateName('location')">
                            <option selected>Seleccione...</option>
                            <option value="QUITO" :selected="true">QUITO</option>
                            <option value="MANTA">MANTA</option>
                            <option value="GUAYAQUIL">GUAYAQUIL</option>
                            <option value="LOS CHILLOS">LOS CHILLOS</option>
                            <option value="CUMBAYA">CUMBAYA</option>
                            </select>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
            <div class="row mt-2">
                <div class="col text-end">
                    <button class="btn btn-success" @click="showView(2)">
                        Siguiente <i class="fa-solid fa-chevron-right"></i>
                    </button>
                </div>
            </div>
            <br />
        </div>

    </div>
</template>
<script>
// confiData
import confData from ".././conf.js";

export default {
    name: 'NameTab',
    emits: ['updateName', 'showView'],
    props: {
        migration_data: {
            type: Object,
            required: true
        },
        taking_data: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            taking_name: '',
            location: '',
            locationsName: confData.locationsName
        }
    },
    methods: {
        updateName() {
            this.taking_name = this.taking_name ? this.taking_name.toUpperCase() : '';
            this.$emit('updateName', {
                takingName: this.taking_name,
                location: this.location
            });
        },
        showView(view) {
            this.$emit('showView', view);
        }
    }, mounted() {
        this.taking_name = this.taking_data.name;
    }
};
    </script>