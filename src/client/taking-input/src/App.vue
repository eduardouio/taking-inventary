<template>
  <div class="navbar bg-slate-300">
    <div class="navbar-start">
      <div class="dropdown">
        <label tabindex="0" class="btn btn-ghost btn-circle text-blue-700">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /></svg>
        </label>
        <ul tabindex="0" class="menu menu-lg dropdown-content mt-3 z-[1] p-1 shadow bg-base-100 rounded-box w-400">
          <li><a> <i class="fas fa-list text-blue-700"></i> Listado Tomas</a></li>
          <li><a> <i class="fas fa-list-check text-blue-700"></i> Histórico <span class="badge">Toma 122</span></a></li>
          <li><a> <i class="fas fa-list-check text-blue-700"></i> Información Grupo</a></li>
          <li><a class="text-danger"> <i class="fas fa-power-off"></i>  Cerrar Sesión</a></li>
        </ul>
      </div>
      Toma 122
    </div>
    <div class="navbar-end">
      <div class="dropdown dropdown-end">
        <label tabindex="0" class="btn btn-ghost btn-circle avatar">
          <div class="w-5 rounded-full text-info">
            <i class="fas fa-user fa-xl"></i>
          </div>
          <small class="text-blue-700">Evillota</small>
        </label>
        <ul tabindex="0" class="menu menu-lg dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-500">
          <li><a> <i class="fas fa-gear text-blue-700"></i> Configuraciones</a></li>
          <li><a class="text-danger"> <i class="fas fa-power-off"></i>  Cerrar Sesión</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
const csrf_token = 'este_es_el_token_de_seguridad';
const url = 'esta_es_la_url';
const base_url = '';

import "bootstrap/dist/css/bootstrap.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";

import Loader from "./components/Loader.vue";
import NavBar from "./components/NavBar.vue";
import SearchForm from "./components/SearchForm.vue";
import ProductDescription from "./components/ProductDescription.vue";
import ReportTaking from "./components/ReportTaking.vue";
import FormTaking from "./components/FormTaking.vue";
import FormGroup from './components/FormGroup.vue';
import FormProduct from './components/FormProduct.vue';

export default {
  name: 'App',
  components: {
    Loader,
    NavBar,
    SearchForm,
    ProductDescription,
    FormTaking,
    ReportTaking,
    FormGroup,
    FormProduct,
  },
  data() {
    return {
      team: null,
      products: null,
      user: null,
      taking: null,
      base_url: base_url,
      url: url,
      server_status: {
        response: null,
        issue_type: '',
        img_ok: base_url + '/static/img/ok.jpg',
        img_error: base_url + '/static/img/error.jpg',
        message: '',
      },
      current_item: null,
      report: [],
      csrf_token: csrf_token,
      have_team: true,
      report_update: false,
      show_status_message: true,
      show_view: {
        loader: true,
        search_form: false,
        product_form: false,
        group_form: false,
        taking_form: false,
        report_info: false,
        product_description: false,
        status_message: false,
      },
      disable_button_send: false,
    }
  },
  methods: {
    getData() {
      const xhr = new XMLHttpRequest();
      xhr.open('GET', this.base_url + this.url);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      xhr.onload = () => {
        if (xhr.status === 200) {
          const data = JSON.parse(xhr.responseText);
          this.taking = data.taking;
          this.team = data.team;
          this.products = data.products;
          this.user = data.user;
          this.show_view.loader = false;
          this.server_status.issue_type = 'success';
          this.server_status.message = 'Completado correctamente';
          this.server_status.response = data;
          this.have_team = Boolean(this.team.fields.warenhouse_assistant);
        }
      };
      xhr.onerror = () => {
        this.show_view.loader = true;
        this.server_status.response = null;
        this.server_status.issue_type = 'error';
        this.server_status.message = 'Error al cargar los datos -> ' + xhr.statusText;
      };
      xhr.send();
    },
    saveReport() {
      this.show_view.loader = true;
      this.server_status.response = null;
      const xhr_1 = new XMLHttpRequest();
      xhr_1.open('POST', this.base_url + '/takings/add-report/');
      xhr_1.setRequestHeader('Content-Type', 'application/json');
      xhr_1.setRequestHeader('X-CSRFToken', this.csrf_token);
      xhr_1.onload = () => {
        this.show_view.report_info = true;
        this.server_status.response = xhr_1.responseText;
        if (xhr_1.status === 201) {
          this.server_status.message = xhr_1.responseText;
        } else if (xhr_1.status === 400) {
          this.server_status.message = xhr_1.responseText;
          this.server_status.issue_type = 'warning';
        }
        else {
          this.server_status.response = null;
          this.server_status.issue_type = 'error';
          this.server_status.message = 'Error al cargar los datos -> ' + xhr_1.responseText;
        }
      };
      xhr_1.onerror = () => {
        this.server_status.response = null;
        this.server_status.issue_type = 'error';
        this.server_status.message = 'Error al cargar los datos -> ' + xhr_1.responseText;
      };

      xhr_1.send(JSON.stringify({
        report: this.report,
        taking: this.taking,
        user: this.user,
        team: this.team,
      }));

    },
    switchView(template_name) {
      this.show_view = {
        loader: false,
        search_form: false,
        product_form: false,
        group_form: false,
        taking_form: false,
        report_info: false,
        product_description: false,
        status_message: false,
        [template_name]: true,
      };
    },
    updateTeam(team) {
      this.team = team;
      this.show_view.loader = true;
      this.server_status.response = null;
      const xhr_team = new XMLHttpRequest();
      xhr_team.open('POST', this.base_url + '/accounts/update-team/');
      xhr_team.setRequestHeader('Content-Type', 'application/json');
      xhr_team.setRequestHeader('X-CSRFToken', this.csrf_token);
      xhr_team.onload = () => {
        this.show_view.loader = false;
        if (xhr_team.status === 200) {
          this.have_team = true;
          this.server_status.issue_type = 'success';
          this.server_status.message = 'Completado correctamente';
          this.server_status.response = xhr_team.responseText;
          this.switchView('search_form');
        } else {
          this.server_status.issue_type = 'error';
          this.server_status.message = 'Error al cargar los datos -> ' + xhr_team.responseText;
          this.switchView('group_form');
        }
      };
      xhr_team.send(JSON.stringify({
        team: this.team,
      }));
    },
    selectItem(product) {
      this.current_item = product;
      this.switchView('product_description');
    },
    deteleItemReport(selected_taking) {
      this.report = this.report.filter((el) => {
        return el !== selected_taking;
      });
      this.switchView('report_info')
    },
  },
  mounted() {
    // Cargamos datos iniciales de la aplicacion
    this.getData();
    window.addEventListener("beforeunload", (e) => {
      e.preventDefault();
      return e.returnValue = 'Esta seguro de salir?, la información se perderá';
    });
  }
}

</script>
<style>
.bordered {
  border: 1px solid #ddd;
}

.row {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin-right: -1px;
  margin-left: -1px;
  margin-top: 2px;
}

.list-group-item {
  padding: 0.25rem 0.03rem;
}

.container {
  padding-right: calc(var(--bs-gutter-x) * 0.01);
  padding-left: calc(var(--bs-gutter-x) * 0.01);
}
</style>
