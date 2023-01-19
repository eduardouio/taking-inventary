from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from sap_migrations.models import SapMigration, SapMigrationDetail


class SapMigrationsAdmin(SimpleHistoryAdmin):
    search_fields = [
        'created',
        'modified',
    ]

    list_display = [
        'is_active',
        'id_sap_migration',
        'id_user_created',
        'created',
        'modified',
        'id_user_updated',
    ]
    
    
class SapMigrationDetailAdmin(SimpleHistoryAdmin):
    search_fields = [
        'name',
        'warenhouse_name',
        'company_name',
    ]

    list_display = [
        'id_sap_migration',
        'name',
        'warenhouse_name',
        'company_name',
        
    ]


admin.site.register(SapMigration, SapMigrationsAdmin)
admin.site.register(SapMigrationDetail, SapMigrationDetailAdmin)
