# Generated by Django 2.0.1 on 2018-02-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0006_auto_20180206_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50)),
                ('document', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FileUnit',
        ),
    ]