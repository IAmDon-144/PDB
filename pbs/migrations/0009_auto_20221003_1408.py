# Generated by Django 3.1.3 on 2022-10-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbs', '0008_fider_fiderno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fider',
            name='fiderNo',
            field=models.IntegerField(blank=True),
        ),
    ]