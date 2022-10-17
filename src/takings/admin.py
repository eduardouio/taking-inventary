from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from takings.models import Taking, TakinDetail


class TakinDetailInline(admin.TabularInline):
    model=TakinDetail


class TakingModelAdmin(SimpleHistoryAdmin):
    inlines = [
        TakinDetailInline
    ]
    search_fields = [
        'user_manager__username',
        'user_manager__first_name',
        'user_manager__last_name',
    ]
    list_display = [
        'id_taking',
        'id_sap_migration',
        'user_manager',
        'location',
        'created',
        'is_active',
    ]


class TakinDetailAdmin(SimpleHistoryAdmin):
    search_fields = [
        'account_code__name',
        'account_code__ean_13_code',
        'location',
    ]
    list_display = [
        'pk',
        'id_taking',
        'account_code',
        'location',
        'quantity',
        'id_team',
        'is_complete',
        
    ]
    

admin.site.register(Taking, TakingModelAdmin)
admin.site.register(TakinDetail, TakinDetailAdmin)

