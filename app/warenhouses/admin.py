from django.contrib import admin
from warenhouses.models import Warenhouse
from simple_history.admin import SimpleHistoryAdmin


class WarenhouseAdmin(SimpleHistoryAdmin):

    fields = (
        'id_warenhouse_number',
        'name',
        'ruc_enterprise',
        'enterprise_name',
        'notes',
        'is_active'
    )

    list_display = (
        'id_warenhouse_number',
        'name',
        'enterprise_name',
        'is_active',
        'created',
        'modified',
        'id_user'
    )

    search_fields = [
        'name',
        'enterprise_name'
    ]


admin.site.register(Warenhouse, WarenhouseAdmin)
