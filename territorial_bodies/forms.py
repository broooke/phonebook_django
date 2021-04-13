from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.utils.translation import gettext, gettext_lazy as _

from .models import Department, Customer, Subdepartment


class signinForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Введите имя пользователя', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Пароль пользователя', help_text='Введите пароль пользователя', strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
    error_messages = {
        'invalid_login': _(
            "Введите корректные данные"
        ),
        'inactive': _("Данный аккаунт неактивен"),
    }
    class Meta:
        model = User
        fields = ('username', 'password',)


class addCustomerForm(forms.ModelForm):
    name = forms.CharField(label="ФИО", required=True)
    role = forms.IntegerField(label="Роль", help_text="0-Начальник, 1-Зам. начальника, 2-Советники, 3-Остальные должности", required=True)
    class Meta:
        model = Customer
        fields = ('name', 'position', 'city_phone_number','inner_phone_number', 'fax', 'email','role', 'subdepartment', )



class addSubdepartmentForm(forms.ModelForm):
    name = forms.CharField(label="Наименование отдела", required=True)
    class Meta:
        model = Subdepartment
        fields = ('name',)
