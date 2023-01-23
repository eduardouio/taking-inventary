# taking-inventary
<ul>
    <li>Validar que solo exista un taking activo en la base</li>
</ul>

# cargar informacion de prueba en el repo
./manage.py shell < tests/test_data/load_test_data.py 

# 

create view v_unique_product_sale
as
select sms.account_code,
	sum(sms.on_hand),
	sum(sms.on_order),
	sum(sms.is_commited),
	SUM(sms.avaliable)
from sap_migrations_sapmigrationdetail sms where  sms.avaliable > 0
group by sms.account_code 