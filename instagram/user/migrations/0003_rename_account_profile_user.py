# Generated by Django 4.1.4 on 2022-12-26 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_profile_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='account',
            new_name='user',
        ),
    ]
