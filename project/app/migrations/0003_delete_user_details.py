# Generated by Django 4.2.3 on 2023-08-23 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_details_confirm_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_details',
        ),
    ]
