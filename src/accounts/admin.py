from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from simple_history.admin import SimpleHistoryAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel, Team

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUserModel
    
    list_display=[
        'username',
        'role',
        'email',
        'is_staff',
        'is_active',
    ]
    list_filter = (
        'username',
        'role',
        'email',
        'is_staff',
        'is_active',
    )
    
    fieldsets = (
        ('Información Básica', {
            'fields':(
                'username',
                'password',
                'role',
            )
        }),
        ('Información Adicional',{
            'fields':(
                'first_name',
                'last_name',
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
    
    add_fieldsets=(
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
    search_fields = ('username','role')
    ordering = ('username', 'role')


class TeamAdmin(SimpleHistoryAdmin):
    pass

admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(Team,TeamAdmin)
