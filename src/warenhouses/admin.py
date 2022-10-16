from django.contrib import admin
from warenhouses.models import Warenhouse
from simple_history.admin import SimpleHistoryAdmin


class WarenhouseAdmin(SimpleHistoryAdmin):

    fields = (
        'id_warenhouse_number',
        'name',
        'owner',
        'notes',
        'is_active'
    )

    list_display = (
        'id_warenhouse_number',
        'name',
        'owner',
        'is_active',
        'created',
        'modified',
        'id_user_created',
    )

    search_fields = [
        'name',
        'owner',
        'id_warenhouse_number',
    ]


admin.site.register(Warenhouse, WarenhouseAdmin)
