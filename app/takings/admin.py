from django.contrib import admin
from takings.models import Taking, Team


class TeamModelAdmin(admin.ModelAdmin):
    pass

class TakingModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Taking, TakingModelAdmin)
admin.site.register(Team, TeamModelAdmin)
