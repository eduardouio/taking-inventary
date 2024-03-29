let show_details = true;
let show_product = true;
var base_url = '/sap/api'
var report = null;


// Muestra | Oculta lista bodegas y empresas
function showDetails() {
    button = document.getElementById('btn-show-details');
    document.getElementById('warenhouses-list').hidden = show_details;
    document.getElementById('enterprises-list').hidden = show_details;
    document.getElementById('groups-list').hidden = show_details;
    show_details = !show_details;

    if (show_details) {
        button.className = 'fas fa-eye';
    } else {
        button.className = 'fas fa-eye';
    }
}

// Muestra oculta la imagen del producto
function showProductImg() {
    document.getElementById('image_product').hidden = show_product;
    show_product = !show_product
}

// Obtiene los datos del productos y los datos inciales 
function getProduct(account_code) {
    //ocultamos la imagen de prodyucto
    showProductImg();

    let xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    xhr.open(
        'GET',
        `${base_url}/migration/${id_migration}/taking/${id_taking}/product/${account_code}`
    )
    data = xhr.send();
    xhr.onload = (response) => {
        if (xhr.status === 200) {
            report = xhr.response;
            updateHeaderProduct(report.product.fields);
            insertList(report.query, 'warenhouse_name');
            insertList(report.query, 'company_name');
            insertStocksDetails(report.query, 'warenhouse_name');
            // cargamos los datos de la toma
            getTakings(id_taking, account_code, report.query);

            return report;
        } else {
            alert('Error al comunicarse con el Servidor');
        }
    }
    xhr.onerror = (response) => {
        alert('Error al obtener el reporte')
    }
}

// Actualiza la cabecera de la ficha
function updateHeaderProduct(product) {
    const fields = [
        'ean_13_code',
        'quantity_per_box',
        'account_code',
        'health_register',
    ]
    let product_image = null;
    if (product.image_front) {
        product_image = '/media/' + product.image_front
    } else {
        product_image = '/static/img/generic_product.png';
    }
    document.getElementById('app-product-desc').innerHTML = `
        ${product.name} 
        <br/>
        <small>${product.ean_13_code ? product.ean_13_code : ''}</small>
    `;
    document.getElementById('image_product').innerHTML = `
        <img src="${product_image}" 
            alt="${product.name}"
            style="width:200px;height:auto"
        >
    `;
    fields.forEach((val) => {
        document.getElementById(val).innerText = product[val];
    });
}

// Totaliza los datos del reporte por item
function totalizerValues(query, field) {
    const my_query = query;
    const report = {
        'report': [],
        'total': 0,
    };

    const uniques = query.map((value) => {
        return value.fields[field];
    }).filter((value, index, my_array) => {
        return my_array.indexOf(value) === index;
    });

    uniques.forEach((value) => {
        let my_item = my_query.reduce((accum, current) => {
            if (current.fields[field] === value) {
                return result = accum + current.fields.on_hand;
            }
            return accum;
        }, 0);
        report.report.push({
            'column': value,
            'total': my_item,
        });
    });

    report.total = report.report.reduce((curr, item) => {
        return curr + item.total;
    }, 0);

    return report;
}


// insertar items en la lista de pdoductos
function insertList(query, report_by) {
    let html = '';
    const report = totalizerValues(query, report_by);

    report.report.forEach((value, index) => {
        html += `
        <tr onclick="insertDetails('${report_by}', '${value.column}')">
            <td class="text-center">${index + 1}</td>
            <td>${value.column}</td>
            <td class="text-right">${value.total.toLocaleString('es-EC')}</td>
        </tr>
        `;
    });

    html += `
        <tr class="bg-gradient-success">
            <td colspan="2" class="text-right"><strong>TOTAL:<strong></td>
            <td class="text-right"><strong> ${report.total.toLocaleString('es-EC')} </strong></td>
        </tr>
    `;
    document.getElementById(report_by).innerHTML = html;
}


// Inserta detalle de saldos SAP en la tabla inferior
function insertDetails(report_by , value) {
    let detail_report = ''
    const detail = report.query.filter((item) => {
        if (item.fields[report_by] === value) {
            return true;
        }
    });

    detail.forEach((item, key) => {
        detail_report += `
            <tr>
                <td class="text-center">${key + 1}</td>
                <td>${item.fields.name}</td>
                <td>${item.fields.company_name}</td>
                <td>${item.fields.warenhouse_name} [${item.fields.id_warenhouse_sap_code}] </td>
                <td class="text-right">${item.fields.on_hand.toLocaleString('es-EC')}</td>
            </tr>
        `
    });

    total = detail.reduce((accum, current) => {
        return accum + current.fields.on_hand;
    }, 0);

    detail_report += `
        <tr class="text-right bg-gradient-secondary">
            <td colspan="4">SUMAS</td>
            <td> <strong>${total.toLocaleString('es-EC')}</strong></td>
        </tr>
    `;
    document.getElementById('query_detail').innerHTML = detail_report;
}


// Inserta los detalles de stock en el tab de cuadre
function insertStocksDetails(query, report_by ) {
    let html = '';
    const report = totalizerValues(query, report_by);

    report.report.forEach((value, index) => {
        html += `
        <tr>
            <td class="text-center">${index + 1}</td>
            <td>${value.column}</td>
            <td class="text-right">${value.total.toLocaleString('es-EC')}</td>
        </tr>
        `;
    });

    html += `
        <tr class="bg-gradient-success">
            <td colspan="2" class="text-right"><strong>TOTAL:<strong></td>
            <td class="text-right"><strong> ${report.total.toLocaleString('es-EC')} </strong></td>
        </tr>
    `;
    document.getElementById('current-sale').innerHTML = html;
}

//Obtiene los detalles de la toma
function getTakings(id_taking, account_code, sap_report) {
    let base_url = `/takings/api/taking-detail/taking/${id_taking}/product/${account_code}`;
    let xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    xhr.open('GET',base_url);
    xhr.send();
    xhr.onload = (response) => {
        if (xhr.status == 200) {
            insertTakingsDetails(xhr.response.query, sap_report)
        }
    };
    xhr.onerror = (response) => {
        alert('Error al obtener el reporte')
    }
    // Actualizamos el enlace de reconteo
    document.getElementById('recount-item').href = `/recounts/make/taking/${id_taking}/product/${account_code}`;
    
}

// Inserta el detalle de las tomas en las tablas
function insertTakingsDetails(query, sap_report){    
    let total_taking = 0;
    let html = '';
    query.forEach((value, index)=>{
        html += `
            <tr>
                <td class="text-center">${index + 1}</td>
                <td>${value.team.manager}</td>
                <td class="text-right">${value.detail.fields.taking_total_boxes.toLocaleString('es-EC')}</td>
                <td class="text-right">${value.detail.fields.taking_total_bottles.toLocaleString('es-EC') }</td>
                <td class="text-right">${value.detail.fields.quantity.toLocaleString('es-EC') }</td>
            </tr>
        `;
    });

    let = taking_total_boxes = query.reduce((accum, current)=>{
        return accum += current.detail.fields.taking_total_boxes;
    },0);

    let = taking_total_bottles = query.reduce((accum, current) => {
        return accum += current.detail.fields.taking_total_bottles;
    }, 0);

    let = quantity = query.reduce((accum, current) => {
        return accum += current.detail.fields.quantity;
    }, 0);

    let sap_stock = sap_report.reduce((accum, current) => {
        return accum += current.fields.on_hand;
    }, 0);

    html += `
        <tr class="bg-success text-right">
            <td colspan="2"><strong>SUMAS</strong></td>
            <td class="text-right"><strong>${taking_total_boxes.toLocaleString('es-EC')}</strong></td>
            <td class="text-right"><strong>${taking_total_bottles.toLocaleString('es-EC')}</strong></td>
            <td class="text-right"><strong>${quantity.toLocaleString('es-EC')}</strong></td>
        </tr>
            `

    // actualizamos las pantallas
    document.getElementById('taking-detail').innerHTML = html;
    document.getElementById('total-taking').innerText = quantity;
    document.getElementById('total-sap').innerText = sap_stock;

    // Actualizamos banderas
    let diff = sap_stock - quantity;
    if (diff === 0){
        document.getElementById('message-status').innerHTML = '<span class="text-success">CUADRADO</span>'
        document.getElementById('status-img').innerHTML = '<h2 class="fas fa-check-square text-success"></h2>'
    }else{
        document.getElementById('message-status').innerHTML = '<span class="text-danger">DIFERENCIA</span>'
        document.getElementById('status-img').innerHTML = `<h2>${diff}</h2> <i class="fas fa-exclamation-triangle text-danger"></i>`
    }

    //Actualizamos reporte con novedades
    report_notes = query.filter((curren)=>{
        return curren.detail.fields.notes;
    });

    let html2 = '';
    report_notes.forEach((value, index)=>{
        html2 += `
            <tr>
                <td class="text-center">${index + 1}</td>
                <td>${value.team.manager} - ${value.team.assistant}</td>
                <td>${ value.detail.fields.notes }</td>
                <td class="text-right">${ value.detail.fields.quantity }</td>
            </tr>
        `;
    });

    let = quantity_2 = report_notes.reduce((accum, current) => {
        return accum += current.detail.fields.quantity;
    }, 0);

    html2 += `
        <tr class="bg-success">
            <td colspan="3"><strong>SUMAS</strong></td>
            <td class="text-right"><strong>${quantity_2.toLocaleString('es-EC')}</strong></td>
        </tr>
            `

    document.getElementById('notes-detail').innerHTML = html2;

}   

showDetails();