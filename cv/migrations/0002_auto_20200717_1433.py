# Generated by Django 3.0.7 on 2020-07-17 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.date(1997, 7, 23), verbose_name='Born'),
        ),
    ]
