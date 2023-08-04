const apiBaseUrl = 'http://localhost:8000';

const appConfig = {
    apiBaseUrl: apiBaseUrl,
    dataUrl: apiBaseUrl + '/api/mobile/assistant/id_tk/191/id_tm/908/',
    csrfToken: 'aqui_va_el_csrf_token',
    imgOk: apiBaseUrl + '/static/img/ok.jpg',
    imgError: apiBaseUrl + '/static/img/error.jpg',
}

export default appConfig;