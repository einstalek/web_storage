# Generated by Django 2.0.1 on 2018-02-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0007_auto_20180206_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]
