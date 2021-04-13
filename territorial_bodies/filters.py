import django_filters

from django import forms

from .models import Department

class DepartmentFilter(django_filters.FilterSet):
	name = django_filters.ModelMultipleChoiceFilter(queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple, label='Управления')

	class Meta:
		model = Department
		fields = ['name']