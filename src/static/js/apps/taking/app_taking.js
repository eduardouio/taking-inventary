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
            csrf_token: csrf_token,
            have_team:false,
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
            disable_button_send:false,
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
            this.current_item = product;
            this.switchView('product_description');
        },
        deteleItemReport(selected_taking){
            this.report = this.report.filter((el)=>{
                return el!==selected_taking;
            });
            this.switchView('report_info')
        },saveReport(){
            // Sealizar una sola llama da  al API
            this.switchView('loader');
            this.show_status_message = false;
            this.sendPostRequest(
                this.report,
                'report',
                '/taking/add-report/'
            );
            this.sendPostRequest(
                this.team,
                'team',
                '/accounts/team/update/'
            );
            this.show_view.report_info = true;
            setTimeout(() => {
                this.show_view.loader = false;
            }, 3000);
        },sendPostRequest(data, name, url){
            this.disable_button_send = true;
            const formData = new FormData()
            formData.append(name, JSON.stringify(data));
            formData.append('taking', JSON.stringify(taking.pk));
            formData.append('team', JSON.stringify(this.team));
            let xhr = new XMLHttpRequest
            xhr.open('POST',url);
            xhr.setRequestHeader('X-CSRFToken', this.csrf_token);
            xhr.send(formData); 
            xhr.onload = ()=>{
            if(xhr.status === 201){
                this.server_status.type = 'success';
                this.server_status.message = name + 'Ingresado Correctamente';
            }
            xhr.onerror = function (e) {
                        this.server_status.type = 'error';
                        this.server_status.have_error_message = true;
                        this.disable_button_send = false;
                        console.dir(e);
                        alert("No es posible comunicarse con el servidor, confirme su conección a la red" + e);
                }
            this.server_status.message = xhr.responseText;
        }
        },
    },
    mounted(){
        setTimeout(() => { 
            this.server_status.sended_request = false;
            this.switchView('search_form');
        }, 500);
        window.addEventListener("beforeunload", (e) => {
            e.preventDefault();
            return e.returnValue = 'Esta seguro de salir?, la información se perderá';
        });
    }
});