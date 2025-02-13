# Generated by Django 5.0.6 on 2024-09-01 12:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_stock_stock_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date_received',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(default='Gasul X', max_length=255),
        ),
    ]
