from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models.CustomUserModel import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUserModel
        fields=('username',)


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'picture',
            'first_name',
            'last_name',
            'dni_number',
            'email',
            'role',
            'contact',
        )

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'readonly':'readonly'},
             ),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dni_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(
                attrs={'class': 'form-control', 'readonly':'readonly'}
            ),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),


        }