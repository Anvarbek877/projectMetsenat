# Generated by Django 4.2.7 on 2023-11-07 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_studentsponsor_sponsor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='phone_number',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^\\+998\\d{9}$')], verbose_name='telefon raqami'),
        ),
    ]
