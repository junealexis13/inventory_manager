# Generated by Django 4.1 on 2024-09-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_alter_stock_date_received_alter_stock_stock_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(default='Awesome Gasul', max_length=255),
        ),
    ]
