# Generated by Django 4.0.4 on 2023-04-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0078_alter_stream_is_free'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(editable=False, help_text='id de la configuración', primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(help_text='nombre de la configuración', max_length=100, verbose_name='nombre')),
                ('value', models.CharField(help_text='valor de la configuración', max_length=100, verbose_name='valor')),
            ],
        ),
    ]
