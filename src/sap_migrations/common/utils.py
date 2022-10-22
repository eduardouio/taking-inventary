from sap_migrations.models import SapMigration, SapMigrationDetail
from common.loggin import loggin


def get_migration(id_sap_migration):
    migration = {
        'migration':None,
        'detail':[],
    }
    sap_migration = SapMigration.get(id_sap_migration)
    
    if sap_migration is None:
        loggin('e', 'migarcion {} no existe'.format(id_sap_migration))
        return migration

    loggin('i', 'Obteneniendo detalles de migracion')
    migration['migration'] = sap_migration
    migration['detail'] = SapMigrationDetail.get_by_migration(id_sap_migration)
    return migration
