# Generated by Django 3.1.2 on 2021-02-04 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20210204_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='products',
        ),
    ]
