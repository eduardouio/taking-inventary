from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import Taking, TakinDetail
from common import loggin

def get_migration(id_sap_migration):
    migration = {
        'migration':None,
        'detail':[],
    }
    migration['migration'] = SapMigration.get(id_sap_migration)
    
    if migration['migration'] is None:
        loggin('e', 'migarcion {} no existe'.format(id_sap_migration))
        return migration

    loggin('i', 'Obteneniendo detalles de migracion')
    migration['detail'] = SapMigrationDetail.get_by_migration(id_sap_migration)
    return migration

def get_all_migrations():
    loggin('i', 'Listado todas las migraciones de SAP')
    all_migrations = []
    sap_migrations = SapMigration.objects.all()
    for migration in sap_migrations:
        my_migration = migration.__dict__
        my_migration = {**my_migration, ** SapMigration.get_user(migration)}
        all_migrations.append(my_migration)
    
    return all_migrations

def get_taking(id_taking):
    taking = {
        'taking': None,
        'detail': [],
        'resume': None,
    }
    taking['taking'] = Taking.get(id_taking)
    
    if taking['taking'] is None:
        loggin('e', 'Toma {} no existe'.format(id_taking))
        return taking
    
    loggin('i', 'Obteneniendo detaille de migration {}'.format(id_taking))
    taking['detail'] = TakinDetail.get_by_taking(id_taking)
    return taking

def get_all_takings():
    pass
