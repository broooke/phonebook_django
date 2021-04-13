# Generated by Django 3.1.7 on 2021-04-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorial_bodies', '0003_auto_20210409_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['role']},
        ),
        migrations.AddField(
            model_name='customer',
            name='role',
            field=models.PositiveIntegerField(default=3, verbose_name='Роль'),
        ),
    ]
