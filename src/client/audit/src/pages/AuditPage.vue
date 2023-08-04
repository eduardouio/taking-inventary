<template>
    <div class="container-fluid">
        <NavBar class="bg-light border-bottom" :title="'Revisión Toma 2'" />
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
                                        style="width: 79.2812px;">Costo</th>
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
                                    <td class="text-end">12.98</td>
                                    <td class="text-end">1</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">2</td>
                                    <td>AGUA TONICA FEVER TREE GINGER ALE</td>
                                    <td class="text-end">24</td>
                                    <td class="text-end">1756</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">3</td>
                                    <td>VINO TERRUNYO CARMENERE</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">5</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">4</td>
                                    <td>BERONIA VERDEJO RUEDA</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">8</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">5</td>
                                    <td>OPORTO RUBY BARROS</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">6</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">6</td>
                                    <td>VINO TINTO EXPORTACION SELECTO CABERNET SAUVIGNON CARMENERE 1500ML</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">32</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">7</td>
                                    <td>VINO CASILLERO MERLOT</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">5</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">8</td>
                                    <td>VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">2</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">9</td>
                                    <td>VINO NZ SOUTHERN OCEAN SAUV. BLANC MARLBOROUGH</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">1</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">10</td>
                                    <td>VINO CH. CASA SILVA CARMENERE GRAN TERRIOR DE LOS ANDES</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">1</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">11</td>
                                    <td>VINO PORT. LANCERS ROSE</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">1</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">12</td>
                                    <td>VINO ESP. ALBALI TINTO CRIANZA</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">4</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">13</td>
                                    <td>VINO CH. SANTA CAROLINA VSC PREMIUM</td>
                                    <td class="text-end">6</td>
                                    <td class="text-end">1</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">14</td>
                                    <td>VINO EU R. MONDAVI P.S. HERITAGE RED BLEND</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">5</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">15</td>
                                    <td>VINO TINTO CATADOR</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">36</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                    <td class="text-center sorting_1">16</td>
                                    <td>VINO CH. MONTES PINOT NOIR SELEC. LTDA.</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">1</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="odd">
                                    <td class="text-center sorting_1">17</td>
                                    <td>VINO MAIPO VARIETAL MERLOT</td>
                                    <td class="text-end">12</td>
                                    <td class="text-end">1</td>
                                    <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                                </tr>
                                <tr class="even">
                                <td class="text-center sorting_1">18</td>
                                <td>PISCO TABERNERO PURO QUEBRANTA</td>
                                <td class="text-end">12</td>
                                <td class="text-end">54</td>
                                <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                            </tr>
                            <tr class="odd">
                                <td class="text-center sorting_1">19</td>
                                <td>VINO ITA. BANFI CHIANTI CLASICO</td>
                                <td class="text-end">6</td>
                                <td class="text-end">2</td>
                                <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
                            </tr>
                            <tr class="even">
                                <td class="text-center sorting_1">20</td>
                                <td>AGUA TONICA FEVER TREE GINGER INDIAN PREMIUM</td>
                                <td class="text-end">24</td>
                                <td class="text-end">191</td>
                                <td nowrap>Esta es la Justificacion</td>
                                    <td><i class="fas fa-file"></i> <i class="fas fa-file"></i> <i class="fas fa-file"></i></td>
                                    <td class="text-center"><select>
                                        <option>Aprobar</option>
                                        <option>Rechazar</option>
                                    </select></td>
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
                        CRUCES Y COMENTARIOS
                    </div>
                    </div>
            </div>
            </div>
            <div class="row mt-1"></div>
            <div class="row">
                <div class="col-8 border m-1">
                <div class="card">
                    <div class="card-header text-center bg-light bg-gradient text-primary rounded">
                        DETALLE DE CRUCES
                    </div>
                    </div>
                    <table class="table table-bordered table-condensed table-hover">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th class="bg-danger bg-opacity-50">Sale De</th>
                                <th class="bg-danger bg-opacity-50">Unds</th>
                                <th class="bg-danger bg-opacity-50">Valor</th>
                                <th class="bg-success bg-opacity-50">Entra A</th>
                                <th class="bg-success bg-opacity-50">Unds</th>
                                <th class="bg-success bg-opacity-50">V Valor</th>
                                <th class="bg-secondary bg-opacity-50">Diferencia</th>
                                <th class="bg-secondary bg-opacity-50">Accion</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="text-center">1</td>
                                <td class="bg-danger bg-opacity-25">VINO TINTO CATADOR</td>
                                <td class="bg-danger bg-opacity-25 text-end">3</td>
                                <td class="bg-danger bg-opacity-25 text-end">9.65</td>
                                <td class="bg-success bg-opacity-25">VINO BLANCO CATADOR</td>
                                <td class="bg-success bg-opacity-25 text-end">3</td>
                                <td class="bg-success bg-opacity-25 text-end">9.65</td>
                                <td class="text-end">
                                    <strong class="text-success">0.00</strong>
                                </td>
                                <td class="text-end ">
                                    <select name="" id="">
                                        <option value=""> <i class="fas fa-check"></i> Aceptar</option>
                                        <option value="">Rechazar</option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <td class="text-center">1</td>
                                <td class="bg-danger bg-opacity-25">WISKY SOMETHING SPECIAL</td>
                                <td class="bg-danger bg-opacity-25 text-end">5</td>
                                <td class="bg-danger bg-opacity-25 text-end">100</td>
                                <td class="bg-success bg-opacity-25">WISKY PASSPORT</td>
                                <td class="bg-success bg-opacity-25 text-end">5</td>
                                <td class="bg-success bg-opacity-25 text-end">40.00</td>
                                <td class="text-danger text-end"> <i class="fas fa-warning"></i> <strong>60.00</strong></td>
                                <td class="text-end">
                                    <select name="" id="">
                                        <option value=""> <i class="fas fa-check"></i> Aceptar</option>
                                        <option value="">Rechazar</option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <td class="text-center">1</td>
                                <td class="bg-danger bg-opacity-25">VINO TINTO CATADOR</td>
                                <td class="bg-danger bg-opacity-25 text-end">3</td>
                                <td class="bg-danger bg-opacity-25 text-end">9.65</td>
                                <td class="bg-success bg-opacity-25">VINO BLANCO CATADOR</td>
                                <td class="bg-success bg-opacity-25 text-end">3</td>
                                <td class="bg-success bg-opacity-25 text-end">9.65</td>
                                <td class="text-success text-end">0.00</td>
                                <td class="text-end">
                                    <select name="" id="">
                                        <option value=""> <i class="fas fa-check"></i> Aceptar</option>
                                        <option value="">Rechazar</option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <td class="text-center">1</td>
                                <td class="bg-danger bg-opacity-25">VINO TINTO CATADOR</td>
                                <td class="bg-danger bg-opacity-25 text-end">3</td>
                                <td class="bg-danger bg-opacity-25 text-end">9.65</td>
                                <td class="bg-success bg-opacity-25">VINO BLANCO CATADOR</td>
                                <td class="bg-success bg-opacity-25 text-end">3</td>
                                <td class="bg-success bg-opacity-25 text-end">9.65</td>
                                <td class="text-success text-end">0.00</td>
                                <td class="text-end">
                                    <select name="" id="">
                                        <option value=""> <i class="fas fa-check"></i> Aceptar</option>
                                        <option value="">Rechazar</option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <td class="text-center">1</td>
                                <td class="bg-danger bg-opacity-25">VINO TINTO CATADOR</td>
                                <td class="bg-danger bg-opacity-25 text-end">3</td>
                                <td class="bg-danger bg-opacity-25 text-end">9.65</td>
                                <td class="bg-success bg-opacity-25">VINO BLANCO CATADOR</td>
                                <td class="bg-success bg-opacity-25 text-end">3</td>
                                <td class="bg-success bg-opacity-25 text-end">9.65</td>
                                <td class="text-success text-end">0.00</td>
                                <td class="text-end">
                                    <select name="" id="">
                                        <option value=""> <i class="fas fa-check"></i> Aceptar</option>
                                        <option value="">Rechazar</option>
                                    </select>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col border m-1">
                <div class="card">
                    <div class="card-header text-center bg-light bg-gradient text-primary rounded">
                        ARCHIVOS ADJUNTOS Y COMENTARIOS AUDITORÍA
                    </div>
                    </div>
                    <div class="row">
                        <div class="col-6">
                            <ul>
                                <li class="text-primary"> <i class="fas fa-file-pdf"></i> Arqueo de Caja</li>
                                <li class="text-primary"> <i class="fas fa-file-pdf"></i> Check List de Toma  </li>
                                <li class="text-primary"> <i class="fas fa-file-pdf"></i> Reporte de Consignaciones</li>
                                <li class="text-primary"> <i class="fas fa-file-pdf"></i> Reporte de Toma</li>
                            </ul>
                        </div>
                        <div class="col-6">
                            <textarea name="" id="" rows="10" style="width: 100%;"></textarea>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row m-3 p-3">
                <div class="col text-end">
                    <button class="btn bg-secondary bg-gradient btn-sm"> <i class="fas fa-file-pdf"></i> Descargar Informe</button>
                    &nbsp;
                    <button class="btn bg-secondary bg-gradient btn-sm">Guardar</button>
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