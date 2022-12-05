const { createApp } = Vue

const app = createApp({
    delimiters: ['${','}'],
    data() {
      return {
        warenhouses: all_warenhouses,
        users: all_users,
        current_warenhouse: null,
        current_user: null,
        all_selected: false,
        all_users_selected: false,
        show_tab_warenhouse: true,
        show_report: false,
      }
    },
    methods:{
      selectWarenhouse(warenhouse){
        warenhouse.is_selected = !warenhouse.is_selected;
        this.current_warenhouse = warenhouse;
      },selectAllWarenhouses(){
        let all_selected = !this.all_selected
        this.warenhouses.map(function(warenhouse){
          warenhouse.is_selected = all_selected;
        });
        this.all_selected = !this.all_selected
      },swithTabForm(){
        this.show_tab_warenhouse = !this.show_tab_warenhouse;
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
      },sendData(){
        console.log('Enviamos informacion del Formulario');
        let csrftoken = decodeURI(document.cookie).split(';')[0].split('=')[1];
        const formData = new FormData();
        formData.append('warenhouses', this.warenhouses.filter((el)=>el.is_selected == true).map((whrs)=>whrs.name));
        formData.append('users', this.users.filter((el)=>el.is_selected == true).map((user)=>user.username));
        console.dir(formData);
        fetch('',{
          method: 'POST',
          headers: {'X-CSRFToken': csrftoken},
          body: formData
        })
        .then(reponse =>reponse.json())
        .catch(error=> console.error('Error', error))
        .then(response => console.log('Success', response))
      }
    },mounted: function(){
      console.log('estamos iniciando la aplicacion');
    },computed: {
      totalOnHand(){
        total = 0
        this.warenhouses.forEach(function(element) {
            if (element.is_selected){
              total += element.on_hand;
            }
        });
        return new Intl.NumberFormat().format(total);
      },allSelected(){
      return {
        'btn-success': !this.all_selected,
        'btn-danger': this.all_selected
      }
    },allUsersSelected(){
      return{
       'btn-success': !this.all_users_selected,
        'btn-danger': this.all_users_selected,
      }
    },totalUsers(){
      total = 0;
      this.users.forEach(function(element){
        if (element.is_selected){
          total += 1;
        }
      });
      return total;
    },enterprisesList(){
      let enterprises_list = [];
      this.warenhouses.forEach(function (item){
        if (item.is_selected){
          enterprises_list = enterprises_list.concat(item.owners);
        }
      });
      enterprises_list = enterprises_list.filter(
        function(elem, idx, list){
          return list.indexOf(elem) === idx;
        }
        );
      return enterprises_list.sort();
    },
    }
  });
app.mount('#app');
