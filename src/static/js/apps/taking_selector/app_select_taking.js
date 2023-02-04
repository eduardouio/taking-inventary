const { createApp } = Vue

const app = createApp({
    delimiters: ['${','}'],
    data() {
      return {
        warenhouses: all_warenhouses,
        unique_warenhouses: [],
        users: all_users,
        current_warenhouse: null,
        current_user: null,
        all_selected: false,
        all_users_selected: false,
        show_report: false,
        id_taking:null,
      }
    },
    methods:{
      selectWarenhouse(warenhouse){
        warenhouse.is_selected = !warenhouse.is_selected;
        this.current_warenhouse = warenhouse;
        this.warenhouses.map((curr)=>{
          if (curr.warenhouse_name === warenhouse.warenhouse_name){
            curr.is_selected = warenhouse.is_selected;
          }
        });
      },selectAllWarenhouses(){
        let all_selected = !this.all_selected
        this.unique_warenhouses.map((warenhouse)=>{
          warenhouse.is_selected = all_selected;
        });
        this.warenhouses.map((warenhouse) => {
          warenhouse.is_selected = all_selected;
        });
        
        this.all_selected = !this.all_selected
      },selectAllUsers(){
        let all_selected = !this.all_users_selected;  
        this.users.map(function(user){
          user.is_selected = all_selected;
        });
        this.all_users_selected =! this.all_users_selected;
      },selectUser(user){
        user.is_selected = !user.is_selected;
        this.current_user = user;
        this.show_report = true;
      },async sendData(){
        let csrftoken = decodeURI(document.cookie).split(';')[0].split('=')[1];
        const formData = new FormData();
        formData.append('warenhouses', this.warenhouses.filter((el)=>el.is_selected == true).map((whrs)=>whrs.name));
        formData.append('users', this.users.filter((el)=>el.is_selected == true).map((user)=>user.username));
        let response = await fetch('',{
          method: 'POST',
          headers: {'X-CSRFToken': csrftoken},
          body: formData
        })
        .then(resp=>resp.text());
        setTimeout(() => {
          console.dir(response);
          let taking = JSON.parse(response);
          window.location.replace('/taking/master-detail/' + taking.id_taking);
        }, 600);
      }
    },mounted: function(){
      const unique_warenhouses = this.warenhouses.map(
        (curren)=>curren.warenhouse_name
        ).filter((curren, index, _array)=>_array.indexOf(curren) === index
      );
      this.unique_warenhouses = unique_warenhouses.map((curren, index)=>{
        return {
          'warenhouse_name': curren,
          'is_selected': false,
        }
      });
      
    },computed: {
    allSelected(){
      return {
        'text-success': !this.all_selected,
        'text-danger': this.all_selected
      }
    },allUsersSelected(){
      return{
       'text-success': !this.all_users_selected,
       'text-danger': this.all_users_selected,
      }
    },totalUsersSelected(){
      total = 0;
      this.users.forEach((element) => {
        if (element.is_selected) {
          total += 1;
        }
      });
      return total;
      },totalWarenhousesSelected() {
        total = 0;
        this.unique_warenhouses.forEach((element) => {
          if (element.is_selected) {
            total += 1;
          }
        });
        return total;
      }, enterprisesList(){
        return this.warenhouses
        .filter((curren)=>curren.is_selected)
        .map((curr) => curr.company_name)
        .filter((elem, idx, list)=>list.indexOf(elem) === idx).sort();
    },
    }
  });
app.mount('#app');
