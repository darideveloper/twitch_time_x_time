# Generated by Django 4.0.4 on 2023-02-06 00:33

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_generalpoint_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ranking',
            field=models.ForeignKey(blank=True, default=app.models.Ranking.get_lower, help_text='ranking del usuario', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ranking', verbose_name='ranking'),
        ),
    ]
