import json
import pytest
from sap_migrations.views import APISapMigrationDetail
from takings.models import Taking


@pytest.mark.django_db
class TestAPISapMigrationDetail():
    # Tests that the API handles invalid input values, such as a non-existent id_migration.
    def test_api_handles_invalid_input(self, mocker):
        # Setup
        id_migration = 999
        id_taking = 1
        id_product = 12345
        taking = Taking(
            id_taking=id_taking,
            id_sap_migration_id=1,
            warenhouses=json.dumps(['Bodega 1'])
        )
        expected_response_data = {
            'account_code': id_product,
            'id_migration': id_migration,
            'query': []
        }
        mocker.patch('takings.models.Taking.get', return_value=taking)
        mocker.patch(
            'sap_migrations.models.SapMigrationDetail.objects.filter', return_value=[])

        # Exercise
        response = APISapMigrationDetail().get(
            None, id_migration, id_taking, id_product)

        # Verify
        assert response.status_code == 200
        assert response.json() == expected_response_data

    # # Tests that the API correctly applies the custom filters to the query.
    # def test_api_applies_custom_filters(self, mocker):
    #     # Setup
    #     id_migration = 1
    #     id_taking = 1
    #     id_product = 12345
    #     warenhouses = ['Bodega 1', 'Bodega 2']
    #     taking = Taking(
    #         id_taking=id_taking,
    #         id_sap_migration_id=id_migration,
    #         warenhouses=json.dumps(warenhouses)
    #     )
    #     sap_migration_detail_1 = SapMigrationDetail(
    #         id_sap_migration_detail=1,
    #         id_sap_migration_id=id_migration,
    #         account_code=id_product,
    #         warenhouse_name='Bodega 1',
    #         on_hand=10
    #     )
    #     sap_migration_detail_2 = SapMigrationDetail(
    #         id_sap_migration_detail=2,
    #         id_sap_migration_id=id_migration,
    #         account_code=id_product,
    #         warenhouse_name='Bodega 2',
    #         on_hand=5
    #     )
    #     expected_response_data = {
    #         'account_code': id_product,
    #         'id_migration': id_migration,
    #         'query': [{
    #             'model': 'sap_migrations.sapmigrationdetail',
    #             'pk': 1,
    #             'fields': {
    #                 'id_sap_migration': id_migration,
    #                 'account_code': id_product,
    #                 'warenhouse_name': 'Bodega 1',
    #                 'on_hand': 10
    #             }
    #         }]
    #     }
    #     mocker.patch('takings.models.Taking.get', return_value=taking)
    #     mocker.patch('sap_migrations.models.SapMigrationDetail.objects.filter', return_value=[
    #                  sap_migration_detail_1, sap_migration_detail_2])

    #     # Exercise
    #     response = APISapMigrationDetail().get(
    #         None, id_migration, id_taking, id_product)

    #     # Verify
    #     assert response.status_code == 200
    #     assert response.json() == expected_response_data

    # # Tests that the API handles None values for id_migration, id_taking, and id_product.
    # def test_api_handles_none_values(self, mocker):
    #     # Setup
    #     id_migration = None
    #     id_taking = None
    #     id_product = None
    #     expected_response_data = {
    #         'account_code': None,
    #         'id_migration': None,
    #         'query': []
    #     }

    #     # Exercise
    #     response = APISapMigrationDetail().get(
    #         None, id_migration, id_taking, id_product)

    #     # Verify
    #     assert response.status_code == 200
    #     assert response.json() == expected_response_data

    # # Tests that the API returns an empty query when the warenhouses field is empty.

    # def test_api_handles_empty_warenhouses(self, mocker):
    #     # Setup
    #     id_migration = 1
    #     id_taking = 1
    #     id_product = 12345
    #     taking = Taking(
    #         id_taking=id_taking,
    #         id_sap_migration_id=id_migration,
    #         warenhouses=json.dumps([])
    #     )
    #     expected_response_data = {
    #         'account_code': id_product,
    #         'id_migration': id_migration,
    #         'query': []
    #     }
    #     mocker.patch('takings.models.Taking.get', return_value=taking)

    #     # Exercise
    #     response = APISapMigrationDetail().get(
    #         None, id_migration, id_taking, id_product)

    #     # Verify
    #     assert response.status_code == 200
    #     assert response.json() == expected_response_data

    # # Tests that the API returns the correct data for a valid request.

    # def test_api_returns_correct_data(self, mocker):
    #     # Setup
    #     id_migration = 1
    #     id_taking = 1
    #     id_product = 12345
    #     warenhouses = ['Bodega 1', 'Bodega 2']
    #     taking = Taking(
    #         id_taking=id_taking,
    #         id_sap_migration_id=id_migration,
    #         warenhouses=json.dumps(warenhouses)
    #     )
    #     sap_migration_detail = SapMigrationDetail(
    #         id_sap_migration_detail=1,
    #         id_sap_migration_id=id_migration,
    #         account_code=id_product,
    #         warenhouse_name='Bodega 1',
    #         on_hand=10
    #     )
    #     expected_response_data = {
    #         'account_code': id_product,
    #         'id_migration': id_migration,
    #         'query': [{
    #             'model': 'sap_migrations.sapmigrationdetail',
    #             'pk': 1,
    #             'fields': {
    #                 'id_sap_migration': id_migration,
    #                 'account_code': id_product,
    #                 'warenhouse_name': 'Bodega 1',
    #                 'on_hand': 10
    #             }
    #         }]
    #     }
    #     mocker.patch('takings.models.Taking.get', return_value=taking)
    #     mocker.patch('sap_migrations.models.SapMigrationDetail.objects.filter',
    #                  return_value=[sap_migration_detail])

    #     # Exercise
    #     response = APISapMigrationDetail().get(
    #         None, id_migration, id_taking, id_product)

    #     # Verify
    #     assert response.status_code == 200
    #     assert response.json() == expected_response_data
