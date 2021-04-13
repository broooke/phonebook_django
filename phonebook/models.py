from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField("Управление", max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Subdepartment(models.Model):
    name = models.CharField("Отдел", max_length=500, null=True, blank=True)
    department = models.ManyToManyField(Department, null=True, blank=True, related_name="sub_department")
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']


class Customer(models.Model):
    name = models.CharField("ФИО", max_length=500, null=True, blank=True)
    position = models.CharField("Должность", max_length=500, null=True, blank=True)
    city_phone_number = models.CharField("Городской номер", max_length=150, null=True, blank=True)
    inner_phone_number = models.CharField("Внутренний номер", max_length=150, null=True, blank=True)
    number_room = models.CharField("Номер кабинета", max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    role = models.PositiveIntegerField("Роль", default=3)
    department = models.ForeignKey(Department, max_length=500, null=True, blank=True, on_delete=models.CASCADE, related_name="user_department")
    subdepartment = models.ForeignKey(Subdepartment, max_length=500, null=True, blank=True, on_delete=models.CASCADE, related_name="user_sub_department")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['role']

