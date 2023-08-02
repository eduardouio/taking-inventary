/** Configuraciones iniciales de la app de toma */
const base_url = 'http://localhost:8000'; 

const appConfig = {
    csrfToken: 'token_de_seguridad',
    baseUurl: base_url,
    urlGet: base_url + '/api/mobile/assistant/id_tk/191/id_tm/908/',
    imgOK: base_url + '/static/img/ok.jpg',
    imgError: base_url + '/static/img/error.jpg',
    pageTitle: 'Toma de datos',
    disableSendButton: false,
};

export default appConfig;