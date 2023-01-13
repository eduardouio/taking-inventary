const { createApp } = Vue;

const app = createApp({
    data(){
        return{
            team: team,
            products: my_products,
            user:user,
            taking: taking,
            server_status:{
                response:false,
                type:'',
                img_ok: '/static/img/ok.jpg',
                img_error: '/static/img/error.jpg',
                img_loader: '/static/img/loader.gif',
                class: 'text-success',
                have_warning_message: false,
                have_error_message: false,
                message:'',
            },
            current_item:null,
            report: [],
            current_taking: {
                pk:null,
                taking: taking.pk,
                account_code: null,
                taking_total_boxes:0,
                taking_total_bottles:0,
                notes:null
            },
            csrf_token: csrf_token,
            have_team:false,
            report_update: false,
            show_view: {
                loader: true,
                search_form: false,
                product_form: false,
                group_form: false,
                taking_form: false,
                report: false,
                product_description: false,
                status_message: false,
            },
        }
    },
    methods: {
        switchView(template_name){
            for (let key in this.show_view){
                if(key === template_name){
                    this.show_view[key] = true;
                }else{
                    this.show_view[key] = false;
                }
            }
        },
        selectItem(product){
            console.log('Producto Seleccionado');
            this.current_item = product;
            this.switchView('product_description');
        }
    },
    mounted(){
        setTimeout(() => { 
            this.server_status.sended_request = false;
            this.switchView('search_form');
        }, 1000);

       // window.addEventListener("beforeunload", (e) => {
       //     e.preventDefault();
       //     return e.returnValue = 'Esta seguro de salir?, la información se perderá';
       // });
    }
});