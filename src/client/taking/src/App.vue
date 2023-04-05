<template>
  <div class="bg-dark">
  <div class="container bg-light">
    <loader 
      v-if="show_view.loader"
      :server_status="server_status"
      ></loader>
      <div v-if="!show_view.loader">
        <nav-bar
          :taking="taking"
          :team="team"
          :user="user"
          :report="report"
          @changeView="$event => switchView($event)"
        ></nav-bar>
        <search-form
          class="mt-1"
          :products="products"
          @selectProduct="$event => selectItem($event)"
        ></search-form>
        <product-description v-if="show_view.product_description"
          class="mt-1"
        ></product-description>
      </div>

  </div>
  </div>
</template>

<script>
const base_url = 'http://192.168.1.100:8000';
// const base_url = 'http://192.168.0.37:8000';
import 'bootstrap/dist/css/bootstrap.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import '@fortawesome/fontawesome-free/js/all.min.js';

import Loader from "./components/Loader.vue";
import NavBar from './components/NavBar.vue';
import SearchForm from './components/SearchForm.vue';
import ProductDescription from './components/ProductDescription.vue';

export default {
  name: 'App',
  components: {
    Loader,
    NavBar,
    SearchForm,
    ProductDescription
  },
  data() {
    return {
      team: null,
      products: null,
      user: null,
      taking: null,
      server_status: {
        response: null,
        issue_type: '',
        img_ok: base_url + '/static/img/ok.jpg',
        img_error: base_url + '/static/img/error.jpg',
        img_loader: base_url + '/static/img/loader.gif',
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
    getData(url){
      return fetch(url)
        .then(response => response.json())
        .then(data => {
          return data;
        })
        .catch(error => {
          this.show_view.loader = true;
          this.server_status.response = null;
          this.server_status.issue_type= 'error';
          this.server_status.message = 'Error al cargar los datos -> ' + error ;

        })
    },
    switchView(template_name) {
      alert(template_name);
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
    }, saveReport() {
      // Sealizar una sola llama da  al API
      this.switchView('loader');
      this.show_status_message = false;
      this.sendPostRequest(
        {
          'report': this.report,
          'team': this.team,
          'taking': this.taking,
        },
        '/takings/add-report/'
      );
      this.show_view.report_info = true;
      this.show_view.status_message = true;

      setTimeout(() => {
        this.show_view.loader = false;
      }, 3000);
    }, sendPostRequest(data, url) {
      this.disable_button_send = false;
      const formData = new FormData()
      formData.append('data', JSON.stringify(data));
      let xhr = new XMLHttpRequest
      xhr.open('POST', url);
      xhr.setRequestHeader('X-CSRFToken', this.csrf_token);
      xhr.send(formData);
      xhr.onload = () => {
        if (xhr.status === 201) {
          this.server_status.type = 'success';
          this.server_status.message = 'Ingresado Correctamente';
        }
        if (xhr.status === 400) {
          this.server_status.type = 'error';
          this.server_status.have_error_message = true;
          this.disable_button_send = false;
          this.server_status.message = xhr.responseText;
        }
      }
      xhr.onerror = (e) => {
        this.server_status.have_error_message = true;
        this.server_status.type = 'error';
        this.disable_button_send = false;
        alert("Ocurrió un error, en la aplicación" + e);
      }
      this.server_status.message = xhr.responseText;
    },
  },
  mounted() {
    this.getData(base_url + '/takings/api/taking/32/').then((data) => {
      this.taking = data.taking;
      this.team = data.team;
      this.products = data.products;
      this.user = data.user;
      this.csrf_token = data.csrf_token;
      this.show_view.loader = false;
      this.server_status.issue_type = 'success';
      this.server_status.message = 'Completado correctamente';
      this.server_status.response = data;
    });
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
