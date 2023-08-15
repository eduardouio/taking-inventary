const baseUrl = "http://localhost:8000";
const idTaking = 170;

const confData = {
    "baseUrl": baseUrl,
    "urlData": baseUrl + `/api/common/taking-data/${idTaking}/`,
    "urlUpdateTaking": baseUrl + `/api/takings/update-taking/${idTaking}/`,
    "urlUpdateTeam": baseUrl + `/api/common/add-team-taking/${idTaking}/`,
    "urlRecount": baseUrl + `/api/common/recount/${idTaking}/{accountCode}/`,
    "userData": {
        "username": "Datos",
        "id": 2,
        "firstName": "Eduardo",
        "lastName": "Villota",
        "email": "eduardouio7@gmail.com",
    },
    "headers": {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-CSRFToken": "aqui_va_el_token_csrf",
    }
}

export default confData;