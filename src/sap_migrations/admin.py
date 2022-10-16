from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from sap_migrations.models import SapMigration, SapMigrationDetail


class SapMigrationDetalInline(admin.TabularInline):
    model = SapMigrationDetail

class SapMigrationsAdmin(SimpleHistoryAdmin):
    inlines = [
        SapMigrationDetalInline,
    ]

class SapMigrationDetailAdmin(SimpleHistoryAdmin):
    pass

admin.site.register(SapMigration, SapMigrationsAdmin)
admin.site.register(SapMigrationDetail, SapMigrationDetailAdmin)
