from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from simple_history.admin import SimpleHistoryAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models.CustomUserModel import CustomUserModel
from .models.Team import Team


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel

    list_display = [
        'username',
        'first_name',
        'last_name',
        'role',
        'email',
        'is_staff',
        'is_active',
    ]
    list_filter = (
        'role',
        'is_active',
    )

    fieldsets = (
        ('Información Básica', {
            'fields': (
                'username',
                'password',
                'role',
            )
        }),
        ('Información Adicional', {
            'fields': (
                'first_name',
                'last_name',
                'dni_number',
                'picture',
                'email',
                'contact',
                'notes',
            )
        }),
        ('Permisos', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
            )},
         ))

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'role',
                'notes',
                'is_staff',
                'is_active',
            )}
         ),
    )
    search_fields = [
        'username',
        'role',
        'dni_number',
        'first_name',
        'last_name',
    ]
    ordering = ('username', 'role')


class TeamAdmin(SimpleHistoryAdmin):
    list_display = [
        'id_team',
        'id_taking',
        'group_number',
        'manager',
        'warenhouse_assistant',
        'created',
    ]

    search_fields = [
        'group_number',
        'manager__first_name',
        'manager__last_name',
        'manager__role',
        'warenhouse_assistant',
    ]


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(Team, TeamAdmin)
