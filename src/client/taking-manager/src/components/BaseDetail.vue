<template>
    <div class="container-fluid mt-3 border p-3">
        <div class="row">
            <div class="col-1">
                <span class="badge bg-dark">
                    {{ selected_item.product.fields.type_product }}
                </span>
            </div>
            <div class="col-10 text-center">
                <h4 class="text-primary" id="app-product-desc">
                    {{ selected_item.product.fields.name }} 
                    <br>
                    <small>{{ selected_item.product.fields.ean_13_code }}</small>
                </h4>
            </div>
            <div class="col text-end">
                <button class="btn btn-outline-danger fs-3" @click="showReport">
                    <i class="fas fa-close"></i>
                </button>
            </div>
        </div>
        <div class="row border">
            <div class="col">
                <span class="text-secondary">Cod Contable:</span>
                {{ selected_item.product.fields.account_code  }}
            </div>
            <div class="col">
                <span class="text-secondary">
                    Und Empaque: 
                </span>
                {{ selected_item.product.fields.quantity_per_box }}
            </div>
            <div class="col">
                <span class="text-secondary">Capacidad:</span>
                {{ selected_item.product.fields.capacity }} 
                {{ selected_item.product.fields.unit_measurement }}
            </div>
        </div>
<div class="row">
    <div class="col-3">
        <img 
            :src="base_url + '/media/' + selected_item.product.fields.image_front"
            class="img-thumbnail"
         >
    </div>
    <div class="col ">
        <div class="d-flex align-items-start">
      <div class="nav flex-column nav-pills me-3" id="v-pills-tab" role="tablist" aria-orientation="vertical">
        <button 
            class="nav-link active border" 
            id="v-pills-home-tab" 
            data-bs-toggle="pill" 
            data-bs-target="#v-pills-home"
            role="tab"
            aria-controls="v-pills-home"
            aria-selected="true"> <i class="fas fa-clipboard-check"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TOMA&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</button>
        <button 
            class="nav-link border"  
            id="v-pills-profile-tab" 
            data-bs-toggle="pill" 
            data-bs-target="#v-pills-profile"
            role="tab"
            aria-controls="v-pills-profile"
            aria-selected="false"> <i class="fas fa-warning"></i> &nbsp;NOVEDADES</button>
        <button 
            class="nav-link border" 
            id="v-pills-messages-tab" 
            data-bs-toggle="pill" 
            data-bs-target="#v-pills-messages"
            role="tab"
            aria-controls="v-pills-messages"
            aria-selected="false"><i class="fas fa-warehouse"></i>&nbsp;EXISTENCIAS</button>
      </div>
      <div class="tab-content" id="v-pills-tabContent">
        <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">...</div>
        <div class="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab">...</div>
        <div class="tab-pane fade" id="v-pills-messages" role="tabpanel" aria-labelledby="v-pills-messages-tab">...</div>
      </div>
    </div>

    </div>
</div>
        <div class="" id="my_report_pdf">
            <div class="">
                <div class="row">
                    <div class="col text-center" id="image_product" hidden="">
                        <img src="/media//app/images/products/TEQUILA-ESPUELA-LICOR-DE-AGAVE-CAFE-750ml.jpg"
                            alt="TEQUILA ESPUELA SILVER" style="width:200px;height:auto">
                    </div>
                </div>
                <div class="row border rounded">
                    <div class="col border">
                        <span class="text-secondary">Cod Barras: </span>
                        <span id="ean_13_code">7862117761051</span>
                    </div>
                    <div class="col border">
                        <span class="text-secondary">Und Empaque: </span>
                        <span id="quantity_per_box">12</span>
                    </div>
                    <div class="col border">
                        <span class="text-secondary">Cod:</span>
                        <span id="account_code">02045932711101010750</span>
                    </div>
                    <div class="col border">
                        <span class="text-secondary">Registro: </span>
                        <span id="health_register"></span>
                    </div>
                </div>
                <br>
                <!-- tabs-->
                <ul class="nav nav-tabs nav-pills" id="myTab" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="home-tab" data-toggle="tab" data-target="#home" type="button"
                            role="tab" aria-controls="home" aria-selected="true" style="width: 300px;"> <i
                                class="fas fa-clipboard-list"></i> &nbsp;Estado Toma</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="notes-tab" data-toggle="tab" data-target="#notes" type="button"
                            role="tab" aria-controls="notes" aria-selected="true" style="width: 300px;"><i
                                class="fas fa-sticky-note"></i> &nbsp;Novedades Toma</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="profile-tab" data-toggle="tab" data-target="#profile" type="button"
                            role="tab" aria-controls="profile" aria-selected="false" style="width: 300px;"> <i
                                class="fas fa-boxes"></i> &nbsp; Existencias SAP</button>
                    </li>
                </ul>
                <div class="tab-content" id="myTabContent">
                    <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                        <div class="row">
                            <div class="col-5 border rounded">
                                <div class="row bg-gradient-light">
                                    <div class="col text-center text-secondary">EXISTENCIAS</div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <table class="table table-bordered table-hover">
                                            <thead>
                                                <tr class="text-center bg-gradient-light">
                                                    <th>#</th>
                                                    <th>Bodega</th>
                                                    <th>Cantidad</th>
                                                </tr>
                                            </thead>
                                            <tbody id="current-sale">
                                                <tr>
                                                    <td class="text-center">1</td>
                                                    <td>MATRIZ PLUSBRAND MANTA</td>
                                                    <td class="text-right">175</td>
                                                </tr>

                                                <tr class="bg-gradient-success">
                                                    <td colspan="2" class="text-right">
                                                        <strong>TOTAL:<strong></strong></strong></td>
                                                    <td class="text-right"><strong> 175 </strong></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            <div class="col-7 border">
                                <div class="row bg-gradient-light">
                                    <div class="col text-center text-secondary">TOMA</div>
                                </div>
                                <div class="row text-center">
                                    <div class="col text-center">
                                        <span class="h2 text-secondary" id="total-sap">175</span>
                                    </div>
                                    <div class="col text-center">
                                        <span class="h2 text-primary" id="total-taking">35</span>
                                    </div>
                                    <div class="col text-center" id="status-img">
                                        <h2>140</h2> <i class="fas fa-exclamation-triangle text-danger"></i>
                                    </div>
                                </div>
                                <div class="row text-center">
                                    <div class="col">
                                        <span class="text-secondary">SAP</span>
                                    </div>
                                    <div class="col text-center">
                                        <span class="text-primary">TOMA</span>
                                    </div>
                                    <div class="col text-center" id="message-status"><span
                                            class="text-danger">DIFERENCIA</span></div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <table class="table table-condensed table-bordered table-hover">
                                            <thead>
                                                <tr class="text-center bg-gradient-light">
                                                    <th>#</th>
                                                    <th>Grupo</th>
                                                    <th>Cajas</th>
                                                    <th>Unds</th>
                                                    <th>Total</th>
                                                </tr>
                                            </thead>
                                            <tbody id="taking-detail">
                                                <tr>
                                                    <td class="text-center">1</td>
                                                    <td>MANUEL GREGORIO PACHAY ZAMBRANO</td>
                                                    <td class="text-right">0</td>
                                                    <td class="text-right">35</td>
                                                    <td class="text-right">35</td>
                                                </tr>

                                                <tr class="bg-success text-right">
                                                    <td colspan="2"><strong>SUMAS</strong></td>
                                                    <td class="text-right"><strong>0</strong></td>
                                                    <td class="text-right"><strong>35</strong></td>
                                                    <td class="text-right"><strong>35</strong></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="notes" role="tabpanel" aria-labelledby="notes-tab">
                        <div class="row bg-gradient-light">
                            <div class="col text-center text-secondary">NOVEDADES ENCONTRADAS</div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <table class="table table-condensed table-bordered table-hover">
                                    <thead>
                                        <tr class="text-center bg-gradient-light">
                                            <th>#</th>
                                            <th>Grupo</th>
                                            <th>Observaciones</th>
                                            <th>Unds</th>
                                        </tr>
                                    </thead>
                                    <tbody id="notes-detail">
                                        <tr class="bg-success">
                                            <td colspan="3"><strong>SUMAS</strong></td>
                                            <td class="text-right"><strong>0</strong></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                        <div class="row">
                            <div class="col border rounded">
                                <div class="row">
                                    <div class="col h6 text-center text-secondary">BODEGAS</div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <table class="table table-bordered table-condensed">
                                            <thead>
                                                <tr class="text-center bg-gradient-light">
                                                    <th>#</th>
                                                    <th>Bodega</th>
                                                    <th>Cantidad</th>
                                                </tr>
                                            </thead>
                                            <tbody id="warenhouse_name">
                                                <tr onclick="insertDetails('warenhouse_name', 'MATRIZ PLUSBRAND MANTA')">
                                                    <td class="text-center">1</td>
                                                    <td>MATRIZ PLUSBRAND MANTA</td>
                                                    <td class="text-right">175</td>
                                                </tr>

                                                <tr class="bg-gradient-success">
                                                    <td colspan="2" class="text-right">
                                                        <strong>TOTAL:<strong></strong></strong></td>
                                                    <td class="text-right"><strong> 175 </strong></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            <div class="col border rounded">
                                <div class="row">
                                    <div class="col h6 text-center text-info">EMPRESAS</div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <table class="table table-bordered table-condensed table-hover">
                                            <thead>
                                                <tr class="text-center bg-gradient-light">
                                                    <th>#</th>
                                                    <th>Empresa</th>
                                                    <th>Cantidad</th>
                                                </tr>
                                            </thead>
                                            <tbody id="company_name">
                                                <tr onclick="insertDetails('company_name', 'SERVMULTIMARC CIA. LTDA.')">
                                                    <td class="text-center">1</td>
                                                    <td>SERVMULTIMARC CIA. LTDA.</td>
                                                    <td class="text-right">175</td>
                                                </tr>

                                                <tr class="bg-gradient-success">
                                                    <td colspan="2" class="text-right">
                                                        <strong>TOTAL:<strong></strong></strong></td>
                                                    <td class="text-right"><strong> 175 </strong></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <br>
                        <div class="border rounded">
                            <div class="row">
                                <div class="col text-center text-secondary h6"> REPORTE DETALLADO</div>
                            </div>
                            <div class="row">
                                <div class="col">
                                    <table class="table table-bordered table-condensed">
                                        <thead>
                                            <tr class="text-center bg-gradient-light">
                                                <th>#</th>
                                                <th>Nombre</th>
                                                <th>Empresa</th>
                                                <th>Bodega</th>
                                                <th>Cantidad</th>
                                            </tr>
                                        </thead>
                                        <tbody id="query_detail">
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- /tabs-->
            </div>
        </div>
        <div class=" -footer">
            <div class="container-fluid">
                <div class="row">
                    <div class="col">
                        <a class="btn btn-warning btn-sm" id="recount-item"
                            href="/recounts/make/taking/121/product/02045932711101010750">
                            <i class="fas fa-share"></i> Reconteo Item
                        </a>
                    </div>
                    <div class="col text-right">
                        <button class="btn btn-dark btn-sm" data-dismiss=" ">
                            <i class="fas fa-window-close"></i>
                            Cerrar
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    //Mostamos la informacion adicional usando una tabla maestro detalle en la que se muestra la informacion de los grupos y los productos que se han tomado
    name: 'BaseDetail',
    emits: ['showReport'],
    props: {
        selected_item: {
            type: Object,
            required: true,
        },
        show_view_report: {
            type: Boolean,
            required: true,
        },
        base_url: {
            type: String,
            required: true,
        },
    },methods:{
        showReport(){
            this.$emit('showReport');
        },
    },
}
</script>

<style scoped>
</style>