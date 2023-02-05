# Generated by Django 4.0.4 on 2023-02-04 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_alter_infopoint_options_remove_generalpoint_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalpoint',
            name='info',
            field=models.ForeignKey(default=1, help_text='información del punto', on_delete=django.db.models.deletion.CASCADE, to='app.infopoint', verbose_name='información'),
        ),
    ]
