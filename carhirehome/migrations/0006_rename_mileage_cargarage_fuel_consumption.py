# Generated by Django 4.2.7 on 2023-12-07 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carhirehome', '0005_alter_cargarage_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargarage',
            old_name='mileage',
            new_name='fuel_consumption',
        ),
    ]
