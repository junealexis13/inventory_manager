# Generated by Django 5.0.3 on 2024-06-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0025_alter_stock_stock_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="stock_name",
            field=models.CharField(default="Awesome Gasul", max_length=255),
        ),
    ]
