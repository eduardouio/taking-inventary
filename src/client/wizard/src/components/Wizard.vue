<template>
    <div class="container text-center">
        <div class="row mt-2 shadow-sm">
            <ul class="nav nav-pills nav-fill">
                <li class="nav-item" @click="showView(1)">
                    <a class="nav-link" href="#" :class="{'active':show_views.step1}">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-home"></i>
                        </span>
                        &nbsp;
                        Nombre
                    </a>
                </li>
                <li class="nav-item" @click="showView(2)">
                    <a class="nav-link" href="#" :class="{'active': show_views.step2}">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-warehouse"></i>
                        </span>
                        &nbsp;
                        Bodegas
                    </a>
                </li>
                <li class="nav-item" @click="showView(3)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step3 }">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-users"></i>
                        </span>
                        &nbsp;
                        Grupos
                    </a>
                </li>
                <li class="nav-item" @click="showView(4)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step4 }">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-list-check"></i>
                        </span>
                        &nbsp;
                        Items
                    </a>
                </li>
                <li class="nav-item" @click="showView(5)">
                    <a class="nav-link" href="#" :class="{ 'active': show_views.step5 }">
                        <span class="badge bg-secondary">
                            <i class="fa-solid fa-chevron-down"></i>
                        </span>
                        Resumen
                    </a>
                </li>
            </ul>
        </div>
        <div class="row rounded border mt-2 shadow">
            <!--Paso 1-->
            <div class="row mt-2" v-if="show_views.step1">
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
                            v-model="taking.name" 
                            @blur="updateName"
                            autofocus
                            >
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col text-end">
                            <button class="btn btn-success btn-sm" @click="showView(2)">
                                Siguiente <i class="fa-solid fa-chevron-right"></i>
                            </button>
                        </div>
                    </div>
                    <br/>
                </div>

            </div>
            <!--/Paso 1-->
            <!--Paso 2-->
            <div class="row mt-2" v-if="show_views.step2">
                <h5 class="mt-2">BODEGAS DISPONIBLES</h5>
                <div class="col bg-light">
                    <div class="row">
                        <div class="col">
                            <div class="row">
                                <div class="col-8 mt-2">
                                    <table class="table table-bordered table-hover table-condesed mi_table">
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th>Bodega</th>
                                                <th><i class="fas fa-cogs"></i></th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>1</td>
                                                <td>Genial</td>
                                                <td class="text-danger"><i class="fa-solid fa-minus"></i></td>
                                            </tr>
                                            <tr>
                                                <td>1</td>
                                                <td>Genial</td>
                                                <td class="text-success"><i class="fa-solid fa-check"></i></td>
                                            </tr>
                                            <tr>
                                                <td>1</td>
                                                <td>Genial</td>
                                                <td class="text-danger"><i class="fa-solid fa-minus"></i></td>
                                            </tr>
                                            <tr>
                                                <td>1</td>
                                                <td>Genial</td>
                                                <td class="text-success"><i class="fa-solid fa-check"></i></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="col-4 mt-2">
                                    <div class="card">
                                        <div class="card-body">
                                            <h5 class="card-title text-info">Bodegas Seleccionadas</h5>
                                            <p class="card-text">
                                            <ul class="list-group text-start">
                                                <li class="list-group-item p-1">Guarda Cuenca</li>
                                                <li class="list-group-item p-1">Vinesa 10 De Agosto</li>
                                                <li class="list-group-item p-1">Vinlitoral Parque California</li>
                                                <li class="list-group-item p-1">Guarda Xima</li>
                                                <li class="list-group-item p-1">Sermultimarc</li>
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
                                                <li class="list-group-item p-1">Vinesa S.A.</li>
                                                <li class="list-group-item p-1">Sermultimarc</li>
                                                <li class="list-group-item p-1">Vinlitoral</li>
                                                <li class="list-group-item p-1">Rev Ecuador</li>
                                                <li class="list-group-item p-1">Plusbrand</li>
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
                    <br/>
                </div>

            </div>
            <!--/Paso 2-->
            <!--Paso 3-->
            <div class="row mt-2" v-if="show_views.step3">
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
                    <br/>
                </div>
            </div>
            <!--/Paso 3-->
            <!--Paso 4-->
            <div class="row mt-2" v-if="show_views.step4">
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
            <!--/Paso 4-->
            <!--Paso 5-->
            <div class="row mt-2" v-if="show_views.step5">
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
                        <br/>
                </div>
            </div>
            <!--/Paso 4-->

            <p></p>
        </div>
    </div>
</template>
<script>

export default {
    name: 'Wizard',
    emits: ['updateName',],
    data() {
        return {
        show_views : {
            step1 : true,
            step2 : false,
            step3 : false,
            step4 : false,
            step5 : false,
        },
        taking: {
           name: '',
           description: '',
           warehouses: [],
           groups: [],
           type_products: [],
        }
        }
    },
    props: {
       migration_data: {
           type: Object,
           default: null
       }
    }, methods: {
        showView(step){
            // seteamos todo en false
            for (const key in this.show_views) {
                this.show_views[key] = false;
            }
            let stepName = 'step'+step;
            this.show_views[stepName] = true;
        }, updateName(){
            this.taking.name = this.taking.name.toUpperCase();
            console.log("Primer llamado a u[date]")
            this.$emit('updateName', this.taking.name);
        },//nextmethod
    },//next vue property
};
</script>
<style>
/** table condensed with padding 0 */
.table> :not(caption)>*>* {
    padding: 0.15rem;
}
</style>