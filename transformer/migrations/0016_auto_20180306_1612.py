# Generated by Django 2.0.1 on 2018-03-06 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0015_auto_20180306_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='config_end',
            field=models.TimeField(default=datetime.datetime(1900, 1, 1, 0, 0, 1)),
        ),
        migrations.AlterField(
            model_name='document',
            name='config_start',
            field=models.TimeField(default=datetime.datetime(1900, 1, 1, 0, 0)),
        ),
    ]
