# Generated by Django 4.1.13 on 2024-05-13 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coustomers', '0003_coustomers_joined_date_coustomers_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coustomers',
            new_name='Coustomer',
        ),
    ]