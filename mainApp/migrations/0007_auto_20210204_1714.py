# Generated by Django 3.1.2 on 2021-02-04 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20210204_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='loaction',
            new_name='location',
        ),
    ]