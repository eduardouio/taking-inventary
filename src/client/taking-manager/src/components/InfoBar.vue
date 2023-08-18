<template>
  <div class="container-fluid mt-1 bg-light">
    <div class="row">
      <div class="progress" style="height: 0.2rem;">
        <div class="progress-bar bg-success" role="progressbar" :style="{ 'width': percent_progress + '%' }"
          :aria-valuenow="percent_progress" aria-valuemin="0" aria-valuemax="100"></div>
        AVANCE DE TOMA
      </div>
    </div>
    <div class="row border bg-gardient-secondary rounded bg-gradient-light" style="padding: 5px;">
      <div class="col-10">
        <span class="border rounded p-1 m-1">
          <i class="fas fa-calendar"></i>
          {{ dateStart }}
        </span>
        <span class=" border rounded p-1 m-1">
          <i class="fas fa-location-dot"></i>
          {{ taking.location }}
        </span>
        <span class="border rounded p-1 m-1">
          <i class="fas fa-clock"></i>
          &nbsp;
          <strong>Inicio:</strong>
          {{ taking.hour_start }}
          &nbsp;
          <strong>Fin:</strong>
          {{ taking.hour_end }}
          &nbsp;
          <strong>Duración:</strong>
          {{ lapsed_time }}
          &nbsp;
          <strong>Conteos:</strong>
          {{ recounts.length }}
        </span>
        <span class="border rounded p-1 m-1">
          <span>
            <i class="fas fa-info-circle"></i>
            &nbsp;
            <strong>Estado:</strong>
            &nbsp;
          </span>
          <span v-if="taking.is_active">
            <i class="fas fa-play text-success"></i>&nbsp;
            <span class="text-success">Abierto </span>
          </span>
          <span v-else>
            <i class="fas fa-stop text-danger"></i>&nbsp;
            <span class="text-danger">Cerrado</span>
          </span>
          <span class="m-1">
            <i class="fas fa-refresh"></i>
            {{ syncs.all.length }}
          </span>
          <span class="m-1 text-success" v-if="isShowAllTakings">
            <i class="fas fa-eye"></i>
            TODO
          </span>
          <span class="m-1 text-danger" v-else>
            <i class="fas fa-exclamation-triangle"></i>
            DIFENCIAS
          </span>
        </span>
        <span class="m-1 ">
        <button class="btn btn-light btn-sm border" v-if="taking.is_active" @click="makeRecount">
          <strong v-if="recountConfirm">
            <i class="fas fa-check text-warning"></i>
            Confirmar
          </strong>
          <span v-else>
            <i class="fas fa-share text-warning"></i>
            Reconteo
          </span>
        </button>
        <button class="btn btn-light btn-sm ms-1 me-1 border" v-if="taking.is_active" @click="closeTaking">
          <span v-if="!closeConfirm">
            <i class="fas fa-stop text-danger"></i>
            Cerrar
          </span>
          <strong v-else>
            <i class="fas fa-check text-danger"></i>
            Confirmar
          </strong>
        </button>
        <button class="btn btn-light btn-sm border" @click="showAllTakings">
          <span v-if="isShowAllTakings">
            <i class="fa-solid fa-eye-slash text-warning"></i> &nbsp;
            Listar Diferencias
          </span>
          <span v-else>
            <i class="fas fa-eye text-success"></i>
            Listar Todo
          </span>
        </button>
      </span>
      </div>
      <div class="col text-end">
        <button class="btn btn-outline-dark btn-sm border" @click="downloadReport" v-if="taking.is_active">
          <i class="fas fa-file-excel text-success"></i>
          &nbsp;
          Reporte Reconteo
        </button>
        <div class="btn-group" role="group" v-if="!taking.is_active">
    <button id="btnGroupDrop1" type="button" class="btn btn-outline-dark btn-sm ms-1 me-1 dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
      <i class="fas fa-table text-success"></i> &nbsp;
      Reportes
    </button>
    <ul class="dropdown-menu" aria-labelledby="btnGroupDrop1">
      <li @click="diffReport(true, 'Diferencias')"><span class="dropdown-item"><i class="fas fa-file-excel text-success"></i> Diferencias </span></li>
      <li @click="diffReport(false, 'Consolidado')" :disabled="generatingReport"><span class="dropdown-item"><i class="fas fa-file-excel text-success"></i> Resumen Consolidado </span></li>
      <li @click="extraReport('reportYears', 'Reporte Anadas')" :disabled="generatingReport"><span class="dropdown-item"><i class="fas fa-file-excel text-success"></i> Añadas</span></li>
      <li @click="extraReport('reportEndDate', 'Reprote Fechas')" :disabled="generatingReport"><span class="dropdown-item"><i class="fas fa-file-excel text-success"></i> Caducidades </span></li>
      <li @click="extraReport('reportNews', 'Reporte Novedades')" :disabled="generatingReport"><span class="dropdown-item"><i class="fas fa-file-excel text-success"></i> Novedades </span></li>
      <li @click="extraReport('reportAll', 'Rerporte Detallada')" :disabled="generatingReport"><span class="dropdown-item"><i class="fas fa-file-excel text-success"></i> Detallado </span></li>
    </ul>
  </div>
      </div>
    </div>
  </div>
</template>
<script>
import { utils, writeFile } from 'xlsx';
import axios from 'axios';

export default {
  name: 'InfoBar',
  emits: ['showAllTakings', 'makeRecount', 'closeTaking','changeAutoReload'],
  props: {
    reportTaking: {
      type: Array,
      required: true,
    }, isShowAllTakings: {
      type: Boolean,
      required: true,
    },taking: {
      type: Object,
      required: true,
    },recounts:{
      type: Array,
      required: true,
    },syncs:{
      type: Object,
      required: true,
    }, confData:{
      type:Object,
      required: true,
    },
  }, data() {
    return {
      recountConfirm: false,
      closeConfirm: false,
      generatingReport: false,
      detailedReport: [],
    }
  },
  computed: {
    // items completos
    full() {
      return this.reportTaking.filter(
        item => item.is_complete == true
      ).length;
    }, left_over() {
      return this.reportTaking.filter(
        item => item.is_complete == false
      ).length;
    }, percent_progress() {
      return Math.round((this.full / this.reportTaking.length) * 100);
    }, lapsed_time() {
      if (this.taking.is_active){
        return 'En curso';
      }

      if (!this.taking.hour_start || !this.taking.hour_end) {
        return '00:00';
      }

      const hStart = new Date(`2000-01-01T${this.taking.hour_start}`);
      const hEnd = new Date(`2000-01-01T${this.taking.hour_end}`);
      const lapsed = new Date(hEnd - hStart);

      const hours = lapsed.getUTCHours().toString().padStart(2, '0');
      const minutes = lapsed.getUTCMinutes().toString().padStart(2, '0');
      const seconds = lapsed.getUTCSeconds().toString().padStart(2, '0');

      return `${hours}:${minutes}:${seconds}`;
    },dateStart(){
      let created = this.taking.created.split('T')[0].split('-');
      return `${created[2]}/${created[1]}/${created[0]}`;
    },
  }, methods: {
    showAllTakings() {
      this.$emit('showAllTakings');
    },downloadReport() {
      let report_json = this.reportTaking.filter(
        item => item.is_complete == false
      ).map((item) => {
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
      const name = this.taking.name;
      ws["!cols"] = [{ wch: 25 }, { wch: 80 }, { wch: 15 }, { wch: 15 }, { wch: 10 }, { wch: 10 }];
      ws["!rows"] = [{ hpx: 30 }];

      utils.book_append_sheet(wb, ws, 'Reporte');
      writeFile(wb, 'Reconteo [Toma #' + this.taking.id_taking + ']' + name + '.xlsx');
    }, diffReport(filtedReport, fileName) {
      // Obtenemos el reporte de diferencias
      var filtered = filtedReport;
      let report_json = this.reportTaking.filter((item)=>{
        if (filtered){
          return item.is_complete == false;
        }
        return true;
      }
      ).map((item) => {
        let status = '';
        if (item.sap_stock > item.tk_quantity) {
          status = 'Faltante';
        } else if(item.sap_stock === item.tk_quantity) {
          status = 'Completo';
        }else{
          status = 'Sobrante';
        }
        return {
          'Cod Contable': item.product.account_code,
          'Producto': item.product.name,
          'Cod Barra': item.product.ean_13_code,
          'Cantidad Caja': item.product.quantity_per_box,
          'Uns SAP': item.sap_stock,
          'Uns Conteo': item.tk_quantity,
          'Diferencia': (item.sap_stock - item.tk_quantity) * -1,
          'Estado ': status,
        }
      });
      const wb = utils.book_new();
      const ws = utils.json_to_sheet(report_json);
      const name = this.taking.name;
      ws["!cols"] = [{ wch: 25 }, { wch: 80 }, { wch: 15 }, { wch: 15 }, { wch: 10 }, { wch: 10 }, { wch: 10 }, { wch: 10 }];
      ws["!rows"] = [{ hpx: 30 }];

      utils.book_append_sheet(wb, ws, 'Reporte');
      writeFile(wb, 'Reporte ' + fileName + ' [Toma #' + this.taking.id_taking + ']' + name + '.xlsx');

    },extraReport(typeReport, fileName){
      this.generatingReport = true;
      // Reporte de anadas de los productos
      if (this.detailedReport.length === 0){
          const headers = this.confData.headers;
          axios.get(this.confData.urlReportDetailed, {headers})
          .then(
            (response) => {
              this.detailedReport = response.data;
              this.extraReport(typeReport);
            }
          )
          .catch(
            (error) => {
              console.log(error);
              alert('Error al intentar obtener el reporte');
            }
          )
      }
      
      var report_json = [];
      if ( typeReport === 'reportYears' ){
          report_json = this.detailedReport.filter(
          (item) => {
            return item.year !== null;
          }
        )
      }
      
      if ( typeReport === 'reportEndDate' ){
          report_json = this.detailedReport.filter(
          (item) => {
            return item.date_expiry !== null;
          }
        )
      }

      if ( typeReport === 'reportNews' ){
          report_json = this.detailedReport.filter(
          (item) => {
            return item.notes !== null;
          }
        )
      }
      
        if ( typeReport === 'reportAll' ){
          report_json = this.detailedReport
        }
       
      report_json = report_json.map(
          (item) => {
            return {
              'Cod Contable': item.account_code,
              'Producto': item.name,
              'Unds X Caja': item.quantity_per_box,
              'Añada': item.year,
              'F Vencimiento': item.date_expiry,
              'Observaciobes': item.notes,
              'T Unidades': item.quantity,
              'Responsable': item.user
            }
      });
    
      const wb = utils.book_new();
      const ws = utils.json_to_sheet(report_json);
      ws["!cols"] = [{ wch: 18 }, { wch: 50 }, { wch: 10 }, { wch: 5 },{ wch: 10 }, { wch: 20 }, { wch: 10 }, {wch: 20}];
      ws["!rows"] = [{ hpx: 30 }];
      utils.book_append_sheet(wb, ws, 'Reporte');
      writeFile(wb, `[Toma #${this.taking.id_taking}] ${fileName}.xlsx`);
      this.generatingReport = false;
    },makeRecount() {
      if (!this.recountConfirm) {
        this.recountConfirm = true;
        return
      }
      this.$emit('makeRecount', 'all');
    }, closeTaking() {
      if (!this.closeConfirm) {
        this.closeConfirm = true;
        return
      }
      this.$emit('closeTaking', this.taking.id_taking);
    }, changeAutoReload(){
      this.$emit('changeAutoReload', this.auto_reload);
    } //text mtehod
  }
}
</script>