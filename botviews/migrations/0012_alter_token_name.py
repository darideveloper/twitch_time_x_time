# Generated by Django 4.0.4 on 2023-04-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botviews', '0011_token_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='name',
            field=models.CharField(help_text='Apodo del token', max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]
