# Generated by Django 3.1.3 on 2022-09-27 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PBS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbs.pbs')),
            ],
        ),
        migrations.CreateModel(
            name='Fider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiderNo', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Working', 'Working'), ('Fault', 'Fault')], max_length=10)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbs.complaincenter')),
            ],
        ),
        migrations.AddField(
            model_name='complaincenter',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbs.zonal'),
        ),
    ]
