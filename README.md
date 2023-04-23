## Toma de Inventarios
Aplicación para tomas físicas de inventario, se conecta al ERP y extrae los saldos de los SKUs disponibles en el ERP.

Proporciona un cliente SPA en el que los asistentes realizan el ingreso de los datos de toma previa verificación de las cantidades de los mismos en las bodegas

El sistema realiza un cuadre de las cantidades ingresadas VS las cantidades entregadas por el EPR, muestra por defecto solo las cantidades que no coinciden

### Crear Archivo config/secrets_config.py
```python
BASE_DIR = Path(__file__).resolve().parent.parent
MY_SECRET_KEY = ''
app_database = {
    'default': {
        'ENGINE':'',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 3306'
    },
}
DATABASE = app_database
ERP_CONNECTION = {
    'server': '',
    'user': '',
    'password': '',
    'database': '',
}
MIGRATION_QUERY = ''
```

``` bash
# Realizar migraciones
./manage.py makemigrations
./manage.py migrate
# Cargar datos inciales
./manage.py shell < tests/test_data/seed.py
```

## TODO

### Características a implemetar luego de la primera ronda de pruebas

<ul>
 <li>:white_large_square: <strong>[BUG]</strong> :lady_beetle: Los productos sobrantes no se reinician</li>
 <li>:white_large_square: <strong>[MIGRACIONES]</strong>Convertir modal de las listas en una ventana nueva</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Convertir modal de las listas en una ventana nueva</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Modificar grupos de las tomas</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Mostrar progreso de tomas</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Mostrar cantidad de reconteos</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Mostrar histórico de tomas (conteos y reconteos)</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Mostrar tomas por grupos y envíos de los mismos</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Exportar reporte de novedades</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Al exportar a excell validar que se maruqen como texto los codigos contables y skus</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Permitir justificiar con texto cada una de las diferencias, mostrar luego de que la toma sea cerrada</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Generar PDFs para reconteo automáticamente al realizar el conteo</li>
 <li>:white_large_square: <strong>[TOMAS]</strong> Mostrar como faltante los que quedan sin toma, luego de cerrar el inventario</li>
 <li>:white_large_square: <strong>[TOMA]</strong> Mostrar el total de las tablas</li>
 <li>:white_large_square: <strong>[TOMA]</strong> No mostrar el botón de editar cuando la toma esté cerrada</li>
 <li>:white_large_square: <strong>[TOMA]</strong> Confirmar los reconteos antes</li>
 <li>:white_large_square: <strong>[TOMA]</strong> Permitit comentarios de auditoria en los registros de diferencias</li>
 <li>:white_large_square: <strong>[TOMA]</strong> Codificar los caracteres especiales en el CSV tiene errores al mostrar tildes y ñ</li>
 <li>:white_large_square: <strong>[TOMA]</strong> Al cerrar la toma los que tienen estado **SIN TOMA** debe quedar como **FALTANTE** </li>
 <li>:white_large_square: <strong>[TOMA]</strong> cuando el invnentario esté cerrado mostrar el total de la lista completa </li>
 <li>:white_large_square: <strong>[TOMA]</strong> Realizar una tomas solo para ciertos productos </li>
 <li>:white_large_square: <strong>[TOMA]</strong> Marcar productos perecibles y no perecibles, para que se haga una toma de esos items </li>
 <li>:white_large_square: <strong>[AUDIT]</strong> revisión de tomas y aprovación de las diferencias</li>
 <li>:white_large_square: <strong>[CONSULTA]</strong> cómo se procede con los productos que no se encuentran en la lista</li>
 <li>:white_large_square: <strong>[PRODUCTS]</strong> Cargar imagenes de los productos en la ficha de los productos</li>
 <li>:white_large_square: <strong>[PRODUCTS]</strong> Habilitar modificaciones de productos</li>
 <li>:white_large_square: <strong>[PRODUCTS]</strong> Notificar cuando un producto sea modificado para aceptar la modificación</li>
 <li>:white_large_square: <strong>[SPA]</strong> deshabilitar boton mientras se realiza la petición, no habilitar hasta error o success</li>
 <li>:white_large_square: <strong>[SPA]</strong>Solo listar los productos con diferencias, para que no se pueda buscar en la aplicación</li>
 <li>:white_large_square: <strong>[SPA]</strong> habilitar lector de códigos de barras</li>
 <li>:white_large_square: <strong>[SPA]</strong> No mostrar menú de GESTOR</li>
 <li>:white_large_square: <strong>[SPA]</strong> Agregar botón de regreso a tomas</li>
 <li>:white_large_square: <strong>[SPA]</strong> Agregar botón de cierre de sesión</li>
 <li>:white_large_square: <strong>[SPA]</strong> Mostar posición en la lista cuando se muestre el detalle al dar click en la lista</li>
 <li>:white_large_square: <strong>[SPA]</strong> Mostrar el histórico de las tomas en los clientes</li>
 <li>:white_large_square: <strong>[SPA]</strong> Mejorar experiencia de usuario al actualizar los inventarios</li>
 <li>:white_large_square: <strong>[DB]</strong> Cruzar los datos de las tomas VS inventario, buscar si existen datos que no corresponden a la toma</li>
 <li>:white_large_square: <strong>[DB]</strong> Examinar producos que no aparecen en el listado segun correo</li>
  <li>:white_large_square: <strong>[DB]</strong> nuevo perfil de encargado de la tienda para que pueda cerrar las novedades</li>
</ul>


#### consulta para obtener e detalle de novedades, de forma provisional

``` sql
select 
	pp.account_code ,
	pp."name" ,
	tt.taking_total_boxes,
	tt.taking_total_bottles,
	at2.manager_id,
	ac.first_name,
	ac.last_name,
	tt.notes
from takings_takindetail tt 
inner join products_product pp on pp.id_product  = tt.account_code_id 
inner join accounts_team at2 on at2.id_team  = tt.id_team_id 
inner join accounts_customusermodel ac on ac.id  = at2.manager_id 
where tt.id_taking_id = 31 and tt.notes is not  null;
```

WHISKY ROYAL SALUTE 21AÑOS->6

cerrar por el status del producto
VINO ARG. E.G.FAMILIA GASCON MALBEC 

-- Seleccionar las tables de la base
SELECT
  'DROP TABLE IF EXISTS ' || tablename || ' CASCADE;' 
from
  pg_tables WHERE schemaname = 'public';

 --
DROP TABLE IF EXISTS accounts_customusermodel_groups CASCADE;
DROP TABLE IF EXISTS accounts_historicalteam CASCADE;
DROP TABLE IF EXISTS accounts_customusermodel CASCADE;
DROP TABLE IF EXISTS accounts_customusermodel_user_permissions CASCADE;
DROP TABLE IF EXISTS auth_group_permissions CASCADE;
DROP TABLE IF EXISTS auth_permission CASCADE;
DROP TABLE IF EXISTS django_content_type CASCADE;
DROP TABLE IF EXISTS accounts_team CASCADE;
DROP TABLE IF EXISTS guardian_groupobjectpermission CASCADE;
DROP TABLE IF EXISTS django_admin_log CASCADE;
DROP TABLE IF EXISTS django_migrations CASCADE;
DROP TABLE IF EXISTS django_session CASCADE;
DROP TABLE IF EXISTS guardian_userobjectpermission CASCADE;
DROP TABLE IF EXISTS products_historicalproduct CASCADE;
DROP TABLE IF EXISTS auth_group CASCADE;
DROP TABLE IF EXISTS recounts_recounttakings CASCADE;
DROP TABLE IF EXISTS takings_historicaltakindetail CASCADE;
DROP TABLE IF EXISTS sap_migrations_historicalsapmigrationdetail CASCADE;
DROP TABLE IF EXISTS products_product CASCADE;
DROP TABLE IF EXISTS recounts_historicalrecountdetails CASCADE;
DROP TABLE IF EXISTS sap_migrations_historicalsapmigration CASCADE;
DROP TABLE IF EXISTS sap_migrations_sapmigration CASCADE;
DROP TABLE IF EXISTS sap_migrations_sapmigrationdetail CASCADE;
DROP TABLE IF EXISTS recounts_historicalrecounttakings CASCADE;
DROP TABLE IF EXISTS recounts_recountdetails CASCADE;
DROP TABLE IF EXISTS takings_historicaltakingjustify CASCADE;
DROP TABLE IF EXISTS takings_takindetail CASCADE;
DROP TABLE IF EXISTS takings_taking_teams CASCADE;
DROP TABLE IF EXISTS takings_historicaltaking CASCADE;
DROP TABLE IF EXISTS takings_takingjustify CASCADE;
DROP TABLE IF EXISTS takings_taking CASCADE;