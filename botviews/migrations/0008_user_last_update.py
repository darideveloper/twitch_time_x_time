# Generated by Django 4.0.4 on 2023-04-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botviews', '0007_rename_settings_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_update',
            field=models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última actualización', verbose_name='Última actualización'),
        ),
    ]
