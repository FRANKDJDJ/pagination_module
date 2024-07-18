# Generated by Django 5.0.6 on 2024-07-10 17:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_alter_mebel_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mebel',
            options={'ordering': ['price'], 'verbose_name': 'Мебель', 'verbose_name_plural': 'Мебель'},
        ),
        migrations.AddField(
            model_name='mebel',
            name='parse_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
