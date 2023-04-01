<template>
  <div>
    <form-group
      :team="team"
      :user="user">
    </form-group>
    <loader
      :server_status="server_status">
    </loader>
    <status-message
      :taking="taking"
      :team="team"
      :user="user"
      :report="report"
      :server_status="server_status"
      @changeView="switchView"
      ></status-message>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import FormGroup from "./components/FormGroup.vue";
import Loader from "./components/Loader.vue";
import StatusMessage from "./components/StatusMessage.vue";  

export default {
  name: 'App',
  components: {
    FormGroup,
    Loader,
    StatusMessage,
  },
  data() {
    return {
      base_url: 'http://localhost:8000/',
      team: team,
      products: my_products,
      user: user,
      taking: taking,
      server_status: {
        response: false,
        type: '',
        img_ok: '/static/img/ok.jpg',
        img_error: '/static/img/error.jpg',
        img_loader: '/static/img/loader.gif',
        class: 'text-success',
        have_warning_message: false,
        have_error_message: false,
        message: '',
      },
      current_item: null,
      report: [],
      csrf_token: csrf_token,
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
    switchView(template_name) {
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
    setTimeout(() => {
      this.server_status.sended_request = false;
      this.switchView('search_form');
    }, 500);
    window.addEventListener("beforeunload", (e) => {
      e.preventDefault();
      return e.returnValue = 'Esta seguro de salir?, la información se perderá';
    });
  }
}
</script>
