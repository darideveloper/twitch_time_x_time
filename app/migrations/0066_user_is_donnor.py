# Generated by Django 4.0.4 on 2023-03-11 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_stream_is_bits_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_donnor',
            field=models.BooleanField(default=False, help_text='indica si el usuario es donador de bits', verbose_name='donador'),
        ),
    ]
