# Generated by Django 4.0.4 on 2023-05-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botcheers', '0005_alter_donation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='time',
            field=models.TimeField(default='00:00:00', help_text='Hora de la donación', verbose_name='Hora'),
        ),
    ]
