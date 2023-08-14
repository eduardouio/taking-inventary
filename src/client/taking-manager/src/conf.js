const baseUrl = "http://localhost:8000";

const confData = {
    "baseUrl": baseUrl,
    "urlData": baseUrl + "/api/common/taking-data/170/",
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