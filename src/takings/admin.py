from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from takings.models import Taking, TakinDetail


class TakinDetailInline(admin.TabularInline):
    model=TakinDetail
    #fields = ('property_value',)
    #readonly_fields = ('property_value',)


class TakingModelAdmin(SimpleHistoryAdmin):
    inlines = [
        TakinDetailInline
    ]


class TakinDetailAdmin(SimpleHistoryAdmin):
    pass

admin.site.register(Taking, TakingModelAdmin)
admin.site.register(TakinDetail, TakinDetailAdmin)

