# Generated by Django 3.1.7 on 2021-04-09 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subordinate_organizations', '0002_auto_20210409_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='department',
            field=models.ForeignKey(blank=True, max_length=500, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_department', to='subordinate_organizations.department'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='position',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='subdepartment',
            field=models.ForeignKey(blank=True, max_length=500, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_sub_department', to='subordinate_organizations.subdepartment', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Управление'),
        ),
        migrations.AlterField(
            model_name='subdepartment',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Отдел'),
        ),
    ]
