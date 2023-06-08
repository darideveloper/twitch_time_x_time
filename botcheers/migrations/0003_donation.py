# Generated by Django 4.0.4 on 2023-05-15 03:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botcheers', '0002_rename_bot_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_chat_link', models.URLField(help_text='Enlace al chat del stream', validators=[django.core.validators.RegexValidator(code='invalid_characters', message='El enlace debe ser un un chat de twitch. Ejemplo: https://www.twitch.tv/minecuak/chat?popout=', regex='https://www.twitch.tv/popout/.*/chat\\?popout=')], verbose_name='Enlace al chat del stream')),
                ('hour', models.IntegerField(help_text='Hora de la donación (de 0 a 23)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)], verbose_name='Hora')),
                ('minute', models.IntegerField(help_text='Minuto de la donación (de 0 a 59)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)], verbose_name='Minuto')),
                ('amount', models.IntegerField(help_text='Cantidad de la donación', verbose_name='Cantidad')),
                ('message', models.CharField(help_text='Mensaje de la donación', max_length=100, verbose_name='Mensaje')),
                ('done', models.BooleanField(default=False, help_text='Indica si la donación ha sido enviada al stream', verbose_name='Donación realizada')),
                ('user', models.ForeignKey(blank=True, help_text='Usuario que ha realizado la donación', null=True, on_delete=django.db.models.deletion.CASCADE, to='botcheers.user', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Donación',
                'verbose_name_plural': 'Donaciones',
            },
        ),
    ]
