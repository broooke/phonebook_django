# Generated by Django 3.1.7 on 2021-03-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_auto_20210319_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='inner_phone_number',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Внутренний номер'),
        ),
    ]
