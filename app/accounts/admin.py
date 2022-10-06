from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUserModel
    
    list_display=[
        'username',
        'position',
        'email',
        'is_staff',
        'is_active',
    ]
    list_filter = (
        'username',
        'position',
        'email',
        'is_staff',
        'is_active',
    )
    
    fieldsets = (
        ('Información Básica', {
            'fields':(
                'username',
                'password',
                'position',
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
                'position',
                'notes',
                'is_staff',
                'is_active',
            )}
        ),
    )
    search_fields = ('username','position')
    ordering = ('username', 'position')


admin.site.register(CustomUserModel, CustomUserAdmin)
