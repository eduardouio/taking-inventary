import { createStore } from "vuex";
import axios from "axios";

const base_url = 'http://localhost:8000'

export default createStore({
    state: {
        reportData: null,
    },
    mutations: {
        SET_REPORT_DATA(state, data) {
            state.reportData = data;
        },
    },
    actions: {
        getJsonData({ commit }) {
            console.log('getJsonData');
            return axios.get(base_url + '/api/migrations/new-report/', {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }).then((response) => {
                commit('SET_REPORT_DATA', response.data);
            }).catch((error) => {
                console.dir(error);
                alert('Error al obtener los datos del reporte' + error);
            });
        }
    }
});

