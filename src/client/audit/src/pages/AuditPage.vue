<template>
    <div class="container-fluid">
        <NavBar class="bg-light border-bottom" :title="'Justificacion Toma 2'" />
        <div class="row m-1"></div>
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-header text-center bg-secondary bg-gradient text-white rounded">
                        NOVEDADES TOMA 10 DE AGOSTO VINESA AGOSTO
                    </div>
                    <div class="table-responsive p-1">
                        <table class="table table-hover table-bordered dataTable no-footer" id="report"
                            aria-describedby="report_info">
                            <thead>
                                <tr class="bg-secondary text-white">
                                    <th class="text-center sorting sorting_asc" tabindex="0" aria-controls="report"
                                        rowspan="1" colspan="1" aria-sort="ascending"
                                        aria-label="#: Activar para ordenar la columna de manera descendente"
                                        style="width: 16.3906px;">#</th>
                                    <th class="text-center text-nowrap sorting" tabindex="0" aria-controls="report"
                                        rowspan="1" colspan="1"
                                        aria-label="Producto: Activar para ordenar la columna de manera ascendente"
                                        style="width: 559.547px;">Producto</th>
                                    <th class="text-center sorting" tabindex="0" aria-controls="report" rowspan="1"
                                        colspan="1" aria-label="SKU: Activar para ordenar la columna de manera ascendente"
                                        style="width: 79.2812px;">Cod Contable</th>
                                    <th class="text-center sorting" tabindex="0" aria-controls="report" rowspan="1"
                                        colspan="1"
                                        aria-label="CxCaja: Activar para ordenar la columna de manera ascendente"
                                        style="width: 57.6562px;">CxCaja</th>
                                    <th class="text-center sorting" tabindex="0" aria-controls="report" rowspan="1"
                                        colspan="1" aria-label="Diff: Activar para ordenar la columna de manera ascendente"
                                        style="width: 35.6094px;">Diff</th>
                                    <th class="text-center sorting" tabindex="0" aria-controls="report" rowspan="1"
                                        colspan="1"
                                        aria-label="Status: Activar para ordenar la columna de manera ascendente"
                                        style="width: 53.4844px;">Justificacion</th>
                                    <th class="text-center sorting" tabindex="0" aria-controls="report" rowspan="1"
                                        colspan="1"
                                        aria-label="Status: Activar para ordenar la columna de manera ascendente"
                                        style="width: 53.4844px;">Archivos</th>
                                        <th class="text-center sorting" tabindex="0" aria-controls="report" rowspan="1"
                                        colspan="1"
                                        aria-label="Status: Activar para ordenar la columna de manera ascendente"
                                        style="width: 53.4844px;">Accion</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="odd">
                                    <td class="text-center sorting_1">1</td>
                                    <td>VINO ALMAVIVA CAB. SAUV.</td>
                                    <td class="text-end">750</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">1</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">2</td>
                                    <td>AGUA TONICA FEVER TREE GINGER ALE</td>
                                    <td class="text-end">200</td>
                                    <td class="text-end">24</td>
                                    <td class="text-end">1756</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">3</td>
                                    <td>VINO TERRUNYO CARMENERE</td>
                                    <td class="text-end">750</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">5</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">4</td>
                                    <td>BERONIA VERDEJO RUEDA</td>
                                    <td class="text-end">750</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">8</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">5</td>
                                    <td>OPORTO RUBY BARROS</td>
                                    <td class="text-end">750</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">6</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">6</td>
                                    <td>VINO TINTO EXPORTACION SELECTO CABERNET SAUVIGNON CARMENERE 1500ML</td>
                                    
                                    <td class="text-end">1500</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">32</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">7</td>
                                    <td>VINO CASILLERO MERLOT</td>
                                    
                                    <td class="text-end">750</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">5</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">8</td>
                                    <td>VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6</td>
                                    
                                    <td class="text-end">750</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">2</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">9</td>
                                    <td>VINO NZ SOUTHERN OCEAN SAUV. BLANC MARLBOROUGH</td>
                                    
                                    <td class="text-end"></td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">1</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">10</td>
                                    <td>VINO CH. CASA SILVA CARMENERE GRAN TERRIOR DE LOS ANDES</td>
                                    
                                    <td class="text-end"></td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">1</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">11</td>
                                    <td>VINO PORT. LANCERS ROSE</td>
                                    
                                    <td class="text-end"></td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">1</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">12</td>
                                    <td>VINO ESP. ALBALI TINTO CRIANZA</td>
                                    
                                    <td class="text-end">750</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">4</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">13</td>
                                    <td>VINO CH. SANTA CAROLINA VSC PREMIUM</td>
                                    
                                    <td class="text-end"></td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">1</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">14</td>
                                    <td>VINO EU R. MONDAVI P.S. HERITAGE RED BLEND</td>
                                    <td class="text-end">750</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">5</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">15</td>
                                    <td>VINO TINTO CATADOR</td>
                                    <td class="text-end">750</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">36</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">16</td>
                                    <td>VINO CH. MONTES PINOT NOIR SELEC. LTDA.</td>
                                    <td class="text-end"></td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">1</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">17</td>
                                    <td>VINO MAIPO VARIETAL MERLOT</td>
                                    
                                    <td class="text-end">750</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">1</td>
                                    <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                                </tr>
                                <tr class="even">
                                <td class="text-center sorting_1">18</td>
                                <td>PISCO TABERNERO PURO QUEBRANTA</td>
                                <td class="text-end">750</td>
                                <td class="text-end">12</td>
                                <td class="text-end">54</td>
                                <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                            </tr>
                            <tr class="odd">
                                <td class="text-center sorting_1">19</td>
                                <td>VINO ITA. BANFI CHIANTI CLASICO</td>
                                
                                <td class="text-end">750</td>
                                <td class="text-end">6</td>
                                <td class="text-end">2</td>
                                <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                            </tr>
                            <tr class="even">
                                <td class="text-center sorting_1">20</td>
                                <td>AGUA TONICA FEVER TREE GINGER INDIAN PREMIUM</td>
                                
                                <td class="text-end">200</td>
                                <td class="text-end">24</td>
                                <td class="text-end">191</td>
                                <td><textarea rows="1" style="width:25rem;"></textarea></td>
                                    <td><input type="file" name="" id=""></td>
                                    <td class="text-center"><i class="fas fa-save"></i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="row m-1"></div>
            <div class="row">
                <div class="col">
                <div class="card">
                    <div class="card-header text-center bg-secondary bg-gradient text-white rounded">
                        Información Adicional De Toma
                    </div>
                    </div>
            </div>
            </div>
            <div class="row mt-1"></div>
            <div class="row">
                <div class="col-8 border m-1">
                <div class="card">
                    <div class="card-header text-center bg-light bg-gradient text-primary rounded">
                        Informe Adicional, Comentarios, Observaciones no detallados anteriormente
                    </div>
                    </div>
                    <textarea style="width: 100%; height: 200px;"></textarea>
                </div>
                <div class="col border m-1">
                <div class="card">
                    <div class="card-header text-center bg-light bg-gradient text-primary rounded">
                        Archivos de Toma, no adjuntados anteriormente
                    </div>
                    </div>
                    <input type="file" name="" id="">
                </div>
            </div>
            <div class="row">
                <div class="col text-end p-1">
                    <button class="btn bg-primary bg-gradient text-white">Enviar Cierre</button>
                </div>
            </div>
        </div>
    </div>
</div></template>
<script>
import NavBar from '../components/NavBar.vue';

export default {
    name: 'AuditPage',
    components: {
        NavBar,
    }
}
</script>