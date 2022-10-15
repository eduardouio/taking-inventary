from django.contrib import admin
from takings.models import Taking, Team, InitialStock


class TeamModelAdmin(admin.ModelAdmin):
    pass

class TakingModelAdmin(admin.ModelAdmin):
    pass

class InitialStockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Taking, TakingModelAdmin)
admin.site.register(Team, TeamModelAdmin)
admin.site.register(InitialStock, InitialStockAdmin)
