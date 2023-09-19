<template>
  <div class="bg-dark">
    <div class="container bg-light">
      <loader
        v-if="show_view.loader"
        :server_status="server_status"
        :show_view="show_view"
        @switchView="$event => switchView($event)">
      </loader>
      <div>
      <nav-bar
        v-if="show_view.loader === false"
        :taking="taking"
        :team="team"
        :user="user"
        :report="report"
        @switchView="$event => switchView($event)">
      </nav-bar>
      <form-group
        v-if="!have_team || show_view.group_form"
        :team="team"
        :user="user"
        :have_team="have_team"
        :show_view="show_view"
        :server_status="server_status"
        @switchView="$event => switchView($event)"
        @updateGroup="$event => updateTeam($event)"
      >
      </form-group>
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
        @switchView="$event => switchView($event)">
      </product-description>
      <form-taking 
      v-if="show_view.taking_form"
      :current_item="current_item"
      :base_url="base_url"
      :report="report"
      @switchView="$event => switchView($event)">
    </form-taking>
    <report-taking
    v-if="show_view.report_info"
    :report="report"
    :team="team"
    :user="user"
    :taking="taking"
    :base_url="base_url"
    :show_view="show_view"
    :server_status="server_status"
    @removeItem="$event => deteleItemReport($event)"
    @switchView="$event => switchView($event)"
    >
  </report-taking>
  <!-- 
        form-product
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
import FormGroup from './components/FormGroup.vue';
import SearchForm from "./components/SearchForm.vue";
import ProductDescription from "./components/ProductDescription.vue";
import FormTaking from "./components/FormTaking.vue";
import ReportTaking from "./components/ReportTaking.vue";
// import FormProduct from './components/FormProduct.vue';

export default {
  name: 'App',
  components: {
    Loader,
    NavBar,
    FormGroup,
    SearchForm,
    ProductDescription,
    FormTaking,
    ReportTaking,
    // FormProduct,
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
      current_item: null,
      report: [],
      csrf_token: appConfig.csrfToken,
      have_team: true,
      report_update: false,
      show_status_message: true,
      disable_button_send: false,
    }
  },
  methods: {
    getData() {
      this.switchView('loader');
      console.log('cargamos toda la data del usuario');
      // change to useng fetch api
      fetch(this.url, {
        method: 'GET',
        headers: appConfig['headers']
      }).then(response => {
        if (response.status === 200) {
          return response.json();
        } else {
          this.show_view.loader = true;
          this.server_status.issue_type = 'error';
          this.server_status.message = `Servidor desconectado ${response.statusText}`;
        }
      }).then(data => {
        this.taking = data.taking;
        this.team = data.team;
        this.products = data.products;
        this.user = data.user;
        this.server_status.issue_type = 'success';
        this.server_status.message = 'Completado correctamente';
        this.server_status.response = data;
        this.have_team = Boolean(this.team.warenhouse_assistant);
        this.switchView('search_form');
      }).catch(error => {
        this.show_view.loader = true;
        this.server_status.response = null;
        this.server_status.issue_type = 'error';
        this.server_status.message = `Servidor desconectado ${error}`;
      });
    },switchView(template_name) {
      console.log('emitimos el evento switchView ' + template_name);
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
      //this.have_team = Boolean(this.team.warenhouse_assistant);
    },
    selectItem(product) {
      this.current_item = product;
      this.switchView('product_description');
    }, deteleItemReport(selected_taking) {
      this.report = this.report.filter((el) => {
        return el !== selected_taking;
      });
      this.switchView('report_info')
    },
  },
  mounted() {
    // Cargamos datos iniciales de la aplicacion
    this.getData();
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
