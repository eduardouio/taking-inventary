const { createApp } = Vue

const app = createApp({
    delimiters: ['${','}'],
    data(){
        return{
            products: products,
            warenhouses:warenhouses,
            filtered_products: [],
            current_item:null,
            show_search: true,
            query_search: '',
        }
    },methods:{
        searchProduct(){
            let result = []
            this.query_search = this.query_search.toUpperCase();

            let params = this.query_search.split(' ');

            for(let i=0; i < this.products.length;i++){
                let search_condition = true;
                for (let j =0 ; j < params.length; j++){
                    if (this.products[i].fields.name.search(params[j]) < 0){
                        search_condition = false;
                }
            }
                if (search_condition){
                    result.push(this.products[i]);
                }
            }
            this.filtered_products = result;    
    },showTaking(item){
        this.show_search = false;
        this.current_item = item;
    },switchView(){
        this.show_search=true;
    },
    },
    mounted(){
        console.log('aplicacion iniciada')
    },computed:{
        
    }
});


app.mount('#app');