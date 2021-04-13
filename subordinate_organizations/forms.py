from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.utils.translation import gettext, gettext_lazy as _

from .models import Department, Customer, Subdepartment

class addCustomerForm(forms.ModelForm):
    name = forms.CharField(label="ФИО", required=True)
    role = forms.IntegerField(label="Роль", help_text="0-Начальник, 1-Зам. начальника, 2-Советники, 3-Остальные должности", required=True)
    class Meta:
        model = Customer
        fields = ('name', 'position', 'city_phone_number','inner_phone_number', 'fax','number_room', 'email','role', 'subdepartment', )



class addSubdepartmentForm(forms.ModelForm):
    name = forms.CharField(label="Наименование отдела", required=True)
    class Meta:
        model = Subdepartment
        fields = ('name',)
