# Generated by Django 3.1.3 on 2022-10-03 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pbs', '0004_auto_20221003_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='noElectricityFor',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='complaincenter',
            name='location',
        ),
        migrations.RemoveField(
            model_name='fider',
            name='fiderNo',
        ),
        migrations.RemoveField(
            model_name='pbs',
            name='location',
        ),
        migrations.RemoveField(
            model_name='report',
            name='complain',
        ),
        migrations.RemoveField(
            model_name='zonal',
            name='location',
        ),
        migrations.AddField(
            model_name='complaincenter',
            name='type',
            field=models.CharField(default='cc', max_length=10),
        ),
        migrations.AddField(
            model_name='fider',
            name='message',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='fider',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='fider',
            name='type',
            field=models.CharField(default='fider', max_length=10),
        ),
        migrations.AddField(
            model_name='pbs',
            name='type',
            field=models.CharField(default='pbs', max_length=10),
        ),
        migrations.AddField(
            model_name='report',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='report',
            name='fidername',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='issue',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='latitude',
            field=models.FloatField(default=1.02),
        ),
        migrations.AddField(
            model_name='report',
            name='longitude',
            field=models.FloatField(default=1.02),
        ),
        migrations.AddField(
            model_name='report',
            name='priority',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='report',
            name='reporterName',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='solved_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Solved', 'Solved')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='report',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='zonal',
            name='type',
            field=models.CharField(default='zonal', max_length=10),
        ),
        migrations.AlterField(
            model_name='fider',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Working', 'Working'), ('Fault', 'Fault'), ('Loadshedding', 'Loadshedding')], max_length=15),
        ),
        migrations.AlterField(
            model_name='report',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='pbs.complaincenter'),
        ),
        migrations.CreateModel(
            name='SubZonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(default='subzonal', max_length=10)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subzonal', to='pbs.zonal')),
            ],
        ),
        migrations.AlterField(
            model_name='complaincenter',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complain', to='pbs.subzonal'),
        ),
    ]
