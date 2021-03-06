# Generated by Django 2.0.1 on 2018-08-01 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('region', models.CharField(max_length=2)),
                ('jk', models.CharField(max_length=100)),
                ('facilitator', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('level', models.IntegerField()),
                ('prerequisite', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='iteration',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program'),
        ),
    ]
