# Generated by Django 3.1.3 on 2022-09-26 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='isOfficers',
            new_name='is_officers',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='isStaff',
            new_name='is_staff',
        ),
    ]
