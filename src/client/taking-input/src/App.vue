<template>
  <div class="bg-dark">
    <div class="container bg-light">
      <loader
        v-if="show_view.loader"
        :server_status="server_status"
        @changeView="$event => switchView($event)">
      </loader>
      <div>
        <nav-bar
          v-if="show_view.loader === false"
          :taking="taking"
          :team="team"
          :user="user"
          :report="report"
          @changeView="$event => switchView($event)">
        </nav-bar>
        <search-form 
          v-if="show_view.search_form"
          class="mt-1" :products="products"
          @selectProduct="$event => selectItem($event)">
        </search-form>
        <product-description
          class="mt-1"
          v-if="show_view.product_description"
          :current_item="current_item"
          :base_url="base_url"
          @changeView="$event => switchView($event)">
        </product-description>
        <form-taking 
          v-if="show_view.taking_form"
          :current_item="current_item"
          :base_url="base_url"
          :report="report"
          @changeView="$event => switchView($event)">
        </form-taking>
        <report-taking
          v-if="show_view.report_info"
          :report="report"
          :team="team"
          :user="user"
          :taking="taking"
          :base_url="base_url"
          :server_status="server_status"
          @removeItem="$event => deteleItemReport($event)"
          @sendReport="$event => saveReport($event)"
        >
        </report-taking>
        <form-group
         v-if="!have_team || show_view.group_form"
         :team="team"
         :user="user"
         @updateGroup="$event => updateTeam($event)"
        >
        </form-group>
        <!--<form-product
          v-if="show_view.product_form"
          :current_item="current_item"
          @updateProduct="$event => updateProduct($event)"
          ></form-product>
          -->
      </div>
    </div>
  </div>
</template>

<script>
import appConfig from "./appConfig";

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
      base_url: appConfig.apiBaseUrl,
      url: appConfig.dataUrl,
      server_status: {
        response: null,
        issue_type: '',
        img_ok: appConfig.imgOk,
        img_error: appConfig.imgError,
        message: '',
      },
      current_item: null,
      report: [],
      csrf_token: appConfig.csrfToken,
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
    getData(){
      const xhr = new XMLHttpRequest();
      xhr.open('GET', this.url);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      xhr.onload = () => {
        if (xhr.status === 200){
          const data = JSON.parse(xhr.responseText);
          this.taking = data.taking;
          this.team = data.team;
          this.products = data.products;
          this.user = data.user;
          this.show_view.loader = false;
          this.server_status.issue_type = 'success';
          this.server_status.message = 'Completado correctamente';
          this.server_status.response = data;
          this.have_team = Boolean(this.team.warenhouse_assistant);
      }};
      xhr.onerror = () => {
        this.show_view.loader = true;
        this.server_status.response = null;
        this.server_status.issue_type = 'error';
        this.server_status.message = 'Error al cargar los datos -> ' + xhr.statusText;
      };
      xhr.send();
    },
    saveReport(){
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
          else{
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
