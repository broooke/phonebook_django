from django.contrib import admin

# Register your models here.

from subordinate_organizations.models import Customer, Department, Subdepartment

admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(Subdepartment)