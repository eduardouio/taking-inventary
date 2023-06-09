<template>
  <div class="container-fluid mt-1 bg-light">
    <div class="row">
      <div class="progress">
        <div class="progress-bar bg-success" role="progressbar" :style="{ 'width': percent_progress + '%' }"
          :aria-valuenow="percent_progress" aria-valuemin="0" aria-valuemax="100"></div>
        AVANCE DE TOMA
      </div>
    </div>
    <div class="row border bg-gardient-secondary rounded bg-gradient-light" style="padding: 5px;">
      <div class="col-8">
        {{ new Date(report.taking.created).toLocaleString('es-Ec') }}
        &nbsp;| &nbsp;
        Estado:
        <span v-if="report.taking.is_active">
          <i class="fas fa-play text-success"></i>&nbsp;
          <span class="text-success">Conteo Abierto, Recibiendo Datos </span>
        </span>
        <span v-else>
          <i class="fas fa-stop text-danger"></i>&nbsp;
          <span class="text-danger">Conteo Cerrado </span>
        </span>
        &nbsp;| &nbsp;
        <button class="btn btn-secondary btn-sm" v-if="report.taking.is_active" @click="makeRecount">
          <strong v-if="recount_confirm">
            <i class="fas fa-check text-warning"></i>
            Confirmar
        </strong>
          <span v-else>
            <i class="fas fa-share text-warning"></i>
            Reconteo
          </span>
        </button>
        &nbsp;
        <button class="btn btn-secondary btn-sm" v-if="report.taking.is_active" @click="closeTaking">
          <span v-if="!close_confirm">      
          <i class="fas fa-stop text-danger"></i>
            Cerrar Toma
          </span>
          <strong v-else>
            <i class="fas fa-check text-danger"></i>
            Confirmar
          </strong>
      </button>
        &nbsp;
        <button class="btn btn-secondary btn-sm" @click="showAllTakings">
          <span v-if="show_all_takings">
            <i class="fa-solid fa-eye-slash text-warning"></i> &nbsp;
            Mostrar Diferencias
          </span>
          <span v-else>
            <i class="fas fa-eye text-success"></i>&nbsp;
            Mostrar Todo
          </span>
        </button>
        &nbsp;
        <span v-if="show_all_takings" class="badge bg-success">
          Se estan mostrando todos los registros
        </span>
        <span v-else class="badge bg-danger">
          Solo se muestran los registros con diferencias
        </span>
      </div>
      <div class="col text-end">
        <strong class="text-info h6">
          {{ report.taking.name }}
        </strong>
        &nbsp;
        <button class="btn btn-outline-secondary btn-sm" @click="downloadReport()">
          <i class="fas fa-file-excel text-success"></i>
          Reporte Diferencias
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import { utils, writeFile } from 'xlsx';


export default {
  name: 'InfoBar',
  emits: ['showAllTakings','makeRecount', 'closeTaking'],
  props: {
    report: {
      type: Object,
      required: true,
    }, show_all_takings: {
      type: Boolean,
      required: true,
    }
  }, data() {
    return {
      recount_confirm: false,
      close_confirm: false,
    }
  },
  computed: {
    // items completos
    full() {
      return this.report.report.filter(
        item => item.is_complete == true
      ).length;
    }, left_over() {
      return this.report.report.filter(
        item => item.is_complete == false
      ).length;
    }, percent_progress() {
      return Math.round((this.full / this.report.report.length) * 100);
    }
  }, methods: {
    showAllTakings() {
      this.$emit('showAllTakings');
  },downloadReport(){
    let report_json = this.report.report.filter(
      item => item.is_complete == false
    ).map((item)=> {
      return {
        'Cod Contable': item.product.account_code,
        'Producto': item.product.name,
        'Cod Barra': item.product.ean_13_code,
        'Cantidad Caja': item.product.quantity_per_box,
        'Cajas': null,
        'Botellas': null,
      }
    });
    
    const wb = utils.book_new();
    const ws = utils.json_to_sheet(report_json);
    ws["!cols"] = [{ wch: 25 }, { wch: 80 }, { wch: 15 }, { wch: 15 }, { wch: 10 }, { wch: 10 }];
    ws["!rows"] = [{hpx: 30}];
      
    utils.book_append_sheet(wb, ws, 'Reporte');
    writeFile(wb, 'Reconteo.xlsx');
  }, makeRecount(){
    if (!this.recount_confirm){
      this.recount_confirm = true;
      return
    }
    this.$emit('makeRecount', 'all');
  },closeTaking(){
    if (!this.close_confirm){
      this.close_confirm = true;
      return
    }
    this.$emit('closeTaking', this.report.taking.id_taking);
  }, //text mtehod
},//nextvue
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.progress {
  --bs-progress-height: 0.3rem;
}
</style>
