# Generated by Django 3.1.3 on 2022-10-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbs', '0014_auto_20221003_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='solved_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
