# Generated by Django 3.1.3 on 2022-10-03 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbs', '0013_auto_20221003_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaincenter',
            name='id',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='fider',
            name='id',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='pbs',
            name='id',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='subzonal',
            name='id',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='zonal',
            name='id',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
