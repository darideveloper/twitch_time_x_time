# Generated by Django 4.0.4 on 2023-08-03 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0095_remove_topdailypoint_position_topdailypoint_amount'),
        ('botcheers', '0026_alter_user_cookies'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='bits_app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.bit', verbose_name='Bits reclamados'),
        ),
    ]
