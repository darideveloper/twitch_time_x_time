# Generated by Django 4.0.4 on 2023-04-10 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0075_pointshistory_week_points_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(editable=False, help_text='id del log', primary_key=True, serialize=False, verbose_name='id')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, help_text='fecha y hora del log', verbose_name='fecha y hora')),
                ('log', models.TextField(help_text='log', verbose_name='log')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]
