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
        Inicio:
        {{ new Date(report.taking.created).toLocaleString('es-Ec') }}
        &nbsp;| &nbsp;
        Estado:
        <span v-if="report.taking.is_active">
          <i class="fas fa-play text-success"></i>&nbsp;
          <span class="text-success">Abierto, Recibiendo Datos </span>
        </span>
        <span v-else>
          <i class="fas fa-stop text-danger"></i>&nbsp;
          <span class="text-danger">Conteo Cerrado </span>
          &nbsp;
          {{ new Date(report.taking.date_end_taking).toLocaleString('es-Ec') }}
          &nbsp; ->
          {{ lapsed_time }} Horas
        </span>
        &nbsp;| &nbsp;
        <!--
          <span @click="changeAutoReload">
            <i class="fas fa-refresh"></i>
            Auto-Update
            <i class="fas fa-power-off text-danger" v-if="!auto_reload"></i>
            <i class="fas fa-power-off text-success" v-else></i>
          </span>
        -->
        <button class="btn btn-secondary btn-sm" @click="Reload()">
          <i class="fa-solid fa-refresh text-primary"></i>
          Actualizar
        </button>
        &nbsp;
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
        <button class="btn btn-outline-secondary btn-sm" @click="downloadReport" v-if="taking_is_open">
          <i class="fas fa-file-excel text-success"></i>
          &nbsp;
          Reporte Reconteo
        </button>
        <button v-else class="btn btn-outline-secondary btn-sm" @click="diffReport">
          <i class="fas fa-file-excel text-success"></i>
          &nbsp;
          Reporte de Diferencias
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import { utils, writeFile } from 'xlsx';


export default {
  name: 'InfoBar',
  emits: ['showAllTakings', 'makeRecount', 'closeTaking','changeAutoReload'],
  props: {
    report: {
      type: Object,
      required: true,
    }, show_all_takings: {
      type: Boolean,
      required: true,
    }, taking_is_open: {
      type: Boolean,
      required: true,
    }, csrf_token: {
      type: String,
      required: true,
    }, auto_reload: {
      type: Boolean,
      required: true,
    }
  }, data() {
    return {
      recount_confirm: false,
      close_confirm: false,
      auto_refresh: false,
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
    }, lapsed_time() {
      const start = new Date(this.report.taking.created);
      const end = new Date(this.report.taking.date_end_taking);
      return parseInt((end - start) / 3600000 * 100) / 100;
    }
  }, methods: {
    showAllTakings() {
      this.$emit('showAllTakings');
    }, Reload() {
      location.reload();
    }, downloadReport() {
      let report_json = this.report.report.filter(
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
      const name = this.report.taking.name;
      ws["!cols"] = [{ wch: 25 }, { wch: 80 }, { wch: 15 }, { wch: 15 }, { wch: 10 }, { wch: 10 }];
      ws["!rows"] = [{ hpx: 30 }];

      utils.book_append_sheet(wb, ws, 'Reporte');
      writeFile(wb, 'Reconteo [Toma #' + this.report.taking.id_taking + ']' + name + '.xlsx');
    }, diffReport() {
      // Obtenemos el reporte de diferencias
      let report_json = this.report.report.filter(
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
      const name = this.report.taking.name;
      ws["!cols"] = [{ wch: 25 }, { wch: 80 }, { wch: 15 }, { wch: 15 }, { wch: 10 }, { wch: 10 }, { wch: 10 }, { wch: 10 }];
      ws["!rows"] = [{ hpx: 30 }];

      utils.book_append_sheet(wb, ws, 'Reporte');
      writeFile(wb, 'Reporte Diferencias [Toma #' + this.report.taking.id_taking + ']' + name + '.xlsx');

    }, makeRecount() {
      if (!this.recount_confirm) {
        this.recount_confirm = true;
        return
      }
      this.$emit('makeRecount', 'all');
    }, closeTaking() {
      if (!this.close_confirm) {
        this.close_confirm = true;
        return
      }
      this.$emit('closeTaking', this.report.taking.id_taking);
    }, changeAutoReload(){
      this.$emit('changeAutoReload', this.auto_reload);
    } //text mtehod
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.progress {
  --bs-progress-height: 0.3rem;
}
</style>
