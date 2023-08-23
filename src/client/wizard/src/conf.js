const idSapMigration = 1;
const baseUrl = "http://localhost:8000";
const urlData = `${baseUrl}/api/common/wizard-assistant/${idSapMigration}/`;
const locationsName = [
    {name: 'CUMBAYA', value: 'CUMBAYA'},
    {name: 'CUENCA', value: 'CUENCA'},
    {name: 'LOS CHILLOS', value: 'LOS CHILLOS'},
    {name: 'MANTA', value: 'MANTA'},
    {name: 'QUITO', value: 'QUITO'},
    {name: 'GUAYAQUIL', value: 'GUAYAQUIL'},
];

const confData = {
    "baseUrl": baseUrl,
    "urlData" : urlData,
    "locationsName": locationsName,
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
};

export default confData;