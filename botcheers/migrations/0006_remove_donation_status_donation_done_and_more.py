# Generated by Django 4.0.4 on 2023-05-15 02:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botcheers', '0005_alter_donation_hour_alter_donation_minute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='status',
        ),
        migrations.AddField(
            model_name='donation',
            name='done',
            field=models.BooleanField(default=False, help_text='Indica si la donación ha sido procesada', verbose_name='Donación procesada'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='stream_chat_link',
            field=models.URLField(help_text='Enlace al chat del stream', validators=[django.core.validators.RegexValidator(code='invalid_characters', message='El enlace debe ser un un chat de twitch. Ejemplo: https://www.twitch.tv/minecuak/chat?popout=', regex='https://www.twitch.tv/popout/.*/chat\\?popout=')], verbose_name='Enlace al chat del stream'),
        ),
    ]
