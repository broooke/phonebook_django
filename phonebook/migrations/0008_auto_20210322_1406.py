# Generated by Django 3.1.7 on 2021-03-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0007_customer_number_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subdepartment',
            name='department',
        ),
        migrations.AddField(
            model_name='subdepartment',
            name='department',
            field=models.ManyToManyField(blank=True, null=True, related_name='sub_department', to='phonebook.Department'),
        ),
    ]
