const idSapMigration = 1;
const baseUrl = "http://localhost:8000";
const My_CSRFToken = "aqui_va_el_token_csrf";
const urlData = `${baseUrl}/api/common/wizard-assistant/${idSapMigration}/`;
const locationsName = [
    {name: 'CUMBAYA', value: 'CUMBAYA', selected:false},
    {name: 'CUENCA', value: 'CUENCA', selected:false},
    {name: 'LOS CHILLOS', value: 'LOS CHILLOS',selected:false},
    {name: 'MANTA', value: 'MANTA',selected:false},
    {name: 'QUITO', value: 'QUITO',selected:false},
    {name: 'GUAYAQUIL', value: 'GUAYAQUIL',selected:false},
];

const confData = {
    "baseUrl": baseUrl,
    "urlData" : urlData,
    "locationsName": locationsName,
    "urlCreateTaking": `${baseUrl}/takings/create/${idSapMigration}`,
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
        "X-CSRFToken": My_CSRFToken,
    }
};

export default confData;