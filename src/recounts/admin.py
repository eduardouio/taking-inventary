from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from recounts.models import RecountTakings, RecountDetails


class RecountsModelAdmin(SimpleHistoryAdmin):
    search_field = [
        'id_taking_id',
        'notes',
    ]

    list_display = [
        'id_taking_id',
        'created',
    ]

class RecountsDetailsAdmin(SimpleHistoryAdmin):
    search_fields = [
        'account_code',
        'id_recount_taking',
    ]


admin.site.register(RecountTakings, RecountsModelAdmin)
admin.site.register(RecountDetails, RecountsDetailsAdmin)
