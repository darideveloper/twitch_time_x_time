# Generated by Django 4.0.4 on 2023-02-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_topdailypoint_options_ranking_max_streams'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePoint',
            fields=[
                ('id', models.AutoField(editable=False, help_text='id del detalle', primary_key=True, serialize=False, verbose_name='id')),
                ('details', models.TextField(help_text='detalles', verbose_name='detalles')),
            ],
            options={
                'verbose_name': 'Tipo de punto',
                'verbose_name_plural': 'Tipos de punto',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['user_name'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
