# Generated by Django 4.0.4 on 2023-04-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0077_delete_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='is_free',
            field=models.BooleanField(default=False, help_text='indica si el stream es free (no restará puntos)', verbose_name='free'),
        ),
    ]
