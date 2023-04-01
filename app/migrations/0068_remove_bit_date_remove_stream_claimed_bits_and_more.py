# Generated by Django 4.0.4 on 2023-04-01 04:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0067_user_first_stream_done_user_referred_user_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bit',
            name='date',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='claimed_bits',
        ),
        migrations.AddField(
            model_name='bit',
            name='stream',
            field=models.ForeignKey(blank=True, help_text='stream al que pertenece el punto', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.stream', verbose_name='stream'),
        ),
        migrations.AddField(
            model_name='bit',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='fecha y hora del punto', verbose_name='fecha y hora'),
        ),
    ]
