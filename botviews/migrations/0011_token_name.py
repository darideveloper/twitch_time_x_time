# Generated by Django 4.0.4 on 2023-04-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botviews', '0010_alter_token_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='name',
            field=models.CharField(default=None, help_text='Apodo del token', max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]
