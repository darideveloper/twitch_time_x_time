# Generated by Django 4.0.4 on 2023-01-23 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_user_ranking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ranking',
            options={'verbose_name': 'Ranking', 'verbose_name_plural': 'Rankings'},
        ),
    ]
