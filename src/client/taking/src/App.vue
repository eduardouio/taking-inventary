<template>
  <div class="bg-dark">
    <div class="container bg-light">
      <loader
        v-if="show_view.loader"
        :server_status="server_status"
        @changeView="$event => switchView($event)">
      </loader>
      <div v-if="!show_view.loader">
        <nav-bar 
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
          :user="user"
          :taking="taking"
          :base_url="base_url"
          :server_status="server_status"
          @removeItem="$event => deteleItemReport($event)"
          @sendReport="$event => saveReport($event)"
        >
        </report-taking>
      </div>
    </div>
  </div>
</template>

<script>
const base_url = "http://192.168.0.25:8000";
const url = "/takings/api/taking/32/"

import "bootstrap/dist/css/bootstrap.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";

import Loader from "./components/Loader.vue";
import NavBar from "./components/NavBar.vue";
import SearchForm from "./components/SearchForm.vue";
import ProductDescription from "./components/ProductDescription.vue";
import FormTaking from "./components/FormTaking.vue";
import ReportTaking from "./components/ReportTaking.vue";

export default {  
  name: 'App',
  components: {
    Loader,
    NavBar,
    SearchForm,
    ProductDescription,
    FormTaking,
    ReportTaking
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
        have_warning_message: false,
        have_error_message: false,
        message: '',
      },
      current_item: null,
      report: [],
      csrf_token: null,
      have_team: false,
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
      xhr.open('GET', this.base_url + this.url);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      xhr.onload = () => {
        console.dir(xhr);
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
          this.csrf_token = data.csrf_token;
 
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
      const xhr_1 = new XMLHttpRequest();
      xhr_1.open('POST', this.base_url + '/takings/add-report/');
      // xhr_1.setRequestHeader('Content-Type', 'application/json');
      xhr_1.setRequestHeader('X-CSRFToken', this.csrf_token);
      xhr_1.onload = () => {
        if (xhr_1.status === 200) {
          const data = JSON.parse(xhr_1.responseText);
          this.show_view.loader = false;
          this.server_status.have_error_message = false;
          console.log(data);
        } else {
          this.show_view.loader = false;
          this.server_status.response = null;
          this.server_status.have_error_message = true;
          this.server_status.issue_type = 'error';
          this.server_status.message = 'Error al cargar los datos -> ' + xhr_1.statusText;
        }
      };
      xhr_1.onerror = () => {
        this.show_view.loader = false;
        this.server_status.response = null;
        this.server_status.have_error_message = true;
        this.server_status.issue_type = 'error';
        this.server_status.message = 'Error al cargar los datos -> ' + xhr_1.statusText;
      };
      
      xhr_1.send(JSON.stringify({
        report: this.report,
        taking: this.taking,
        user: this.user,
        team: this.team,
      }));

    },
    switchView(template_name) {
      console.log(template_name);
      for (let key in this.show_view) {
        if (key === template_name) {
          this.show_view[key] = true;
        } else {
          this.show_view[key] = false;
        }
      }
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
    //window.addEventListener("beforeunload", (e) => {
    //  e.preventDefault();
    //  return e.returnValue = 'Esta seguro de salir?, la información se perderá';
    //});
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
    padding: 0.25rem 0.50rem;
}
</style>
