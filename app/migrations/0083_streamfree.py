# Generated by Django 4.0.4 on 2023-06-02 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0082_alter_comment_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamFree',
            fields=[
                ('id', models.AutoField(editable=False, help_text='id del free extra', primary_key=True, serialize=False, verbose_name='id')),
                ('amount', models.IntegerField(default=1, help_text='cantidad de frees', verbose_name='cantidad')),
                ('user', models.ForeignKey(help_text='usuario  al que se le ha asignado el free', on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Stream Free',
                'verbose_name_plural': 'Streams Free',
            },
        ),
    ]
