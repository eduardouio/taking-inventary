const idTaking = 303;
const idTeam = 1742;
const apiBaseUrl = 'http://localhost:8000';
const csrfToken = 'aqui_va_el_csrf_token';

const appConfig = {
    "apiBaseUrl": apiBaseUrl,
    "dataUrl": `${apiBaseUrl}/api/mobile/assistant/id_tk/${idTaking}/id_tm/${idTeam}/`,
    "csrfToken": csrfToken,
    "imgOk": `${apiBaseUrl}/static/img/ok.jpg`,
    "imgError": `${apiBaseUrl}/static/img/error.jpg`,
    "defaultPicture": `${apiBaseUrl}/static/img/generic_product.png`,
    "updateTeamURL": `${apiBaseUrl}/api/teams/update-team/${idTeam}/`,
    "syncUrl": `${apiBaseUrl}/api/takings-detail/sync/`,
    "headers": {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    }
}

export default appConfig;