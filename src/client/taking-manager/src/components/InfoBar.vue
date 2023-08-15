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
      <div class="col-9">
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
        <button class="btn btn-light btn-sm" v-if="taking.is_active" @click="makeRecount">
          <strong v-if="recountConfirm">
            <i class="fas fa-check text-warning"></i>
            Confirmar
          </strong>
          <span v-else>
            <i class="fas fa-share text-warning"></i>
            Reconteo
          </span>
        </button>
        <button class="btn btn-light btn-sm ms-1 me-1" v-if="taking.is_active" @click="closeTaking">
          <span v-if="!closeConfirm">
            <i class="fas fa-stop text-danger"></i>
            Cerrar
          </span>
          <strong v-else>
            <i class="fas fa-check text-danger"></i>
            Confirmar
          </strong>
        </button>
        <button class="btn btn-light btn-sm" @click="showAllTakings">
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
        <button class="btn btn-outline-dark btn-sm" @click="downloadReport" v-if="taking.is_active">
          <i class="fas fa-file-excel text-success"></i>
          &nbsp;
          Reporte Reconteo
        </button>
        <button v-if="!taking.is_active" class="btn btn-outline-secondary btn-sm" @click="diffReport">
          <i class="fas fa-file-excel text-success"></i>
          &nbsp;
          Diferencias
        </button>
        <button  v-if="!taking.is_active" class="btn btn-outline-secondary btn-sm ms-1 me-1" @click="extraReport('urlReportYears')" :disabled="generatingReport">
          <i class="fas fa-file-excel text-success"></i>
          &nbsp;
          Añadas
        </button>
        <button  v-if="!taking.is_active" class="btn btn-outline-secondary btn-sm" @click="extraReport('urlReportEndDate')" :disabled="generatingReport">
          <i class="fas fa-file-excel text-success"></i>
          &nbsp;
          Caducidades
        </button>

        
      </div>
    </div>
  </div>
</template>
<script>
import { utils, writeFile } from 'xlsx';
import axios from 'axios';
import confData from '../conf';

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
    }, diffReport() {
      // Obtenemos el reporte de diferencias
      let report_json = this.reportTaking.filter(
        item => item.is_complete == false
      ).map((item) => {
        let status = '';
        if (item.sap_stock > item.tk_quantity) {
          status = 'Faltante';
        } else {
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
      writeFile(wb, 'Reporte Diferencias [Toma #' + this.taking.id_taking + ']' + name + '.xlsx');

    }, extraReport(typeReport){
      // Reporte de anadas de los productos
      this.generatingReport = true;
      const headers = this.confData.headers;
      axios.get(this.confData[typeReport], {headers})
      .then((response)=>{
        if (response.status === 200){
          this.makeReport(response.data, typeReport);
        }
      })
      .catch(
        (error) => {
          alert('No hay datos para mostrar');
          console.log(error);
        }
      );
    },makeReport(dataReport, typeReport){
      console.log('Armamos el reporte');
      var report_json = []
      if (typeReport === 'urlReportEndDate'){
        report_json = dataReport.map((item) => {
          return {
            'PK': item.product.id_product,
            'Cod Contable': item.product.account_code,
            'Producto': item.product.name,
            'Fecha Expiracion': item.date_expiry,
            'Unds X Caja': item.product.quantity_per_box,
            'T Unidades': item.quantity,
          }
      });
      }else{
        report_json = dataReport.map((item) => {
          return {
            'PK': item.product.id_product,
            'Cod Contable': item.product.account_code,
            'Producto': item.product.name,
            'Añada': item.year,
            'Unds X Caja': item.product.quantity_per_box,
            'T Unidades': item.quantity,
          }
      });
      }
      
      const wb = utils.book_new();
      const ws = utils.json_to_sheet(report_json);
      ws["!cols"] = [{ wch: 5 }, { wch: 20 }, { wch: 50 }, { wch: 10 },{ wch: 10 }, { wch: 10 }, { wch: 10 }];
      ws["!rows"] = [{ hpx: 30 }];
      utils.book_append_sheet(wb, ws, 'Reporte');
      writeFile(wb, `[Toma #${this.taking.id_taking}] ${typeReport}.xlsx`);
      this.generatingReport = false;
    }, makeRecount() {
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.progress {
  --bs-progress-height: 0.11rem;
}
.btn-sm {
  padding: 0.10rem !important;
  font-size: 0.75rem !important;
}
</style>
