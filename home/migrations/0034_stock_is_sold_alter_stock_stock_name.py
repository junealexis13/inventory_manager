# Generated by Django 5.0.6 on 2024-08-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_stock_stock_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(default='Oh my Gas', max_length=255),
        ),
    ]
