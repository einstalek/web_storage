# Generated by Django 2.0.1 on 2018-02-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0005_auto_20180206_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileunit',
            name='origin_path',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
