# Generated by Django 4.2.10 on 2024-06-02 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_sudo_admin_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sudo_admin_user',
            new_name='Contacts',
        ),
    ]