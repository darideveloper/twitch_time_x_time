# Generated by Django 4.0.4 on 2023-06-29 23:34

import botcheers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botcheers', '0025_alter_user_cookies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cookies',
            field=models.JSONField(default=botcheers.models.get_default_cookies, help_text='Cookies de sesión del usuario', verbose_name='Cookies'),
        ),
    ]
