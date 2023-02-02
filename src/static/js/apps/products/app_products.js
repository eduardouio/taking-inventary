var report = null;

function getProduct(account_code) {
    let xhr = new XMLHttpRequest()
    xhr.responseType = "json";
    xhr.open(
        'GET',
        base_url + account_code + '/migration/' + id_migration
    )
    data = xhr.send();
    xhr.onload = (response) => {
        if (xhr.status === 200) {
            report = xhr.response;
            updateHeaderProduct(report.product.fields);
            insertList(report.query, 'warenhouse_name');
            insertList(report.query, 'company_name');
            return report;
        } else {
            alert('Error al comunicarse con el Servidor');
        }
    }
    xhr.onerror = (response) =>{
        alert('Error al obtener el reporte')
    }
}

function updateHeaderProduct(product) {
    const fields = [
        'ean_13_code',
        'quantity_per_box',
        'account_code',
        'health_register',
    ]
    url_image = product.image_front
    product_image = url_image ? url_image : '/static/img/generic_product.png';
    document.getElementById('app-product-desc').innerHTML = `
        ${product.name} 
        <br/>
        <small>${product.ean_13_code}</small>
    `;
    document.getElementById('image_product').innerHTML = `
        <img src="${ product_image }" 
            alt="${ product.name }"
            style="width:200px;height:auto"
        >
    `;
    fields.forEach((val)=>{
        document.getElementById(val).innerText = product[val];
    });
}

function totalizerValues(query, field) {
    const my_query = query;
    const report = {
        'report': [],
        'total': 0,
    };

    const uniques =  query.map((value) => {
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

    report.total = report.report.reduce((curr, item)=>{
        return curr + item.total;
    },0);

    return report;
}


function insertList(query, report_by){
    let html  = '';
    const report = totalizerValues(query, report_by);
    console.dir(report);
    console.log(report.total);

    report.report.forEach((value,index)=>{
        html += `
        <tr onclick="insertDetails('${report_by}', '${value.column}')">
            <td class="text-center">${index + 1}</td>
            <td>${value.column}</td>
            <td class="text-right">${value.total.toLocaleString('es-EC') }</td>
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

function insertDetails(report_by, value){
    let detail_report = ''

    report.query.forEach((item, key) => {
        detail_report += `
            <tr>
                <td>${key + 1}</td>
                <td>${item.name}</td>
                <td>${item.company_name}</td>
                <td>${item.warenhouse_name} [${item.id_warenhouse_sap_code}] </td>
                <td class="text-right">${item.on_hand}</td>
            </tr>
        `
    });

    detail_report += `
        <tr class="text-right bg-gradient-light">
            <td colspan="4">SUMAS</td>
            <td> <strong>0</strong></td>
        </tr>
    `;
    document.getElementById('query_detail').innerHTML = detail_report;
}



