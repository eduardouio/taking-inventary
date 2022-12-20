from django.core.serializers import serialize
from sap_migrations.models import SapMigration, SapMigrationDetail
import json


class ConsolidateMigration(object):

    def get(self, id_sap_migration):
        report = self.__get_init_report(id_sap_migration)
        if report['status'] is False:
            none_data = {
                'by_products':[],
                'by_owners':[],
                'by_warenhouses':[],
                'table_by_owners':[],
                'table_by_warenhouses':[],
            }
            return {**report, **none_data}

        report.update({
            'by_products': self.__resume('products', report),
            'by_owners': self.__resume('owners', report),
            'by_warenhouses': self.__resume('warenhouses', report),
            'table_by_owners':[],
            'table_by_warenhouses':[],
        })

        for product in report['products']:
            report['table_by_warenhouses'].append(
                self.__reduce(report ,product, 'by_warenhouses')
            )
            report['table_by_owners'].append(
                self.__reduce(report, product, 'by_owners')
            )
        return report
    
    def __reduce(self, report, product, condition):
        item_found = {
                'account_code': product,
                'name': '',
                'on_hand': 0,
                'on_order': 0,
                'is_commited': 0,
                'avaliable': 0,
                'columns':  [],
        }
        
        for column in report[condition]:
                detail = {
                    'name':  column['name'],
                    'on_hand': 0,
                    'on_order': 0,
                    'is_commited': 0,
                    'avaliable': 0,
                }
                for itm in column['values']:
                    if itm.account_code  == product:
                        item_found['name'] = itm.name
                        detail['on_hand'] += itm.on_hand
                        detail['on_order'] += itm.on_order
                        detail['is_commited'] += itm.is_commited
                        detail['avaliable'] += itm.avaliable

                item_found['columns'].append(detail)
                item_found['on_hand'] += detail['on_hand']
                item_found['on_order'] += detail['on_order']
                item_found['is_commited'] += detail['is_commited']
                item_found['avaliable'] += detail['avaliable']

        return item_found

    def __resume(self, keyword, report):
        filtered = []
        fields_keywords = {
            'products': 'account_code',
            'warenhouses': 'warenhouse_name',
            'owners': 'company_name',
        }
        for condition in report[keyword]:
            item_found = {
                'name': '',
                'values': [], 
                'totals':{
                    'name': '',
                    'on_hand': 0,
                    'on_order': 0,
                    'is_commited': 0,
                    'avaliable': 0,
            }}
            for item in report['sap_migration_detail']:
                if condition == item.__dict__[fields_keywords[keyword]]:
                    item_found['totals']['name'] = item.warenhouse_name
                    item_found['totals']['on_hand'] += item.on_hand
                    item_found['totals']['on_order'] += item.on_order
                    item_found['totals']['is_commited'] += item.is_commited
                    item_found['totals']['avaliable'] += item.avaliable
                    item_found['name'] = item.__dict__[fields_keywords[keyword]]
                    item_found['values'].append(item)

            filtered.append(item_found)
        return filtered

    def __get_init_report(self, id_sap_migration):
        report = {
            'sap_migration': None,
            'sap_migration_detail': None,
            'status': False,
            'products': {},
            'warenhouses': {},
            'owners': {},
            'totals': {
                'on_hand': 0,
                'on_order': 0,
                'is_commited': 0,
                'avaliable': 0,
            }
        }
        sap_migration = SapMigration.get(id_sap_migration)
        sap_migration_detail = SapMigrationDetail.get_by_migration(
            id_sap_migration
        )

        if not sap_migration_detail:
            return report
        
        report['sap_migration'] = sap_migration
        report['sap_migration_detail'] = sap_migration_detail

        for item in sap_migration_detail:
            report['totals']['on_hand'] += item.on_hand
            report['totals']['on_order'] += item.on_order
            report['totals']['is_commited'] += item.is_commited
            report['totals']['avaliable'] += item.avaliable

            report['products'].update({
                item.account_code : item.account_code
            })
            report['warenhouses'].update({
                    item.warenhouse_name: item.warenhouse_name
            })
            report['owners'].update({
                item.company_name: item.company_name
            })

        report['products'] = list(report['products'].keys())
        report['owners'] = list(report['owners'].keys())
        report['warenhouses'] = list(report['warenhouses'].keys())
        report['status'] = True

        if sap_migration.have_report is False:
            sap_migration.total_warenhouses = len(report['warenhouses'])
            sap_migration.total_products = len(report['products'])
            sap_migration.total_products_unities = report['totals']['on_hand']
            sap_migration.have_report = True
            sap_migration.report = self.__compress_report(report)
            sap_migration.save()

        return report
    
    def __compress_report(self, report):
        report_json = report.copy()
        del(report_json['sap_migration'])
        del(report_json['sap_migration_detail'])
        return json.dumps(report_json)