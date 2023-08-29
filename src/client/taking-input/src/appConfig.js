const idTaking = 303;
const idTeam = 1742;
const apiBaseUrl = 'http://localhost:8000';

const appConfig = {
    apiBaseUrl: apiBaseUrl,
    dataUrl: `${apiBaseUrl}/api/mobile/assistant/id_tk/${idTaking}/id_tm/${idTeam}/`,
    csrfToken: 'aqui_va_el_csrf_token',
    imgOk: `${apiBaseUrl}/static/img/ok.jpg`,
    imgError: `${apiBaseUrl}/static/img/error.jpg`,
    defaultPicture: `${apiBaseUrl}/static/img/generic_product.png`,
}

export default appConfig;