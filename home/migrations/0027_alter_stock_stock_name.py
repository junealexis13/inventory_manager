# Generated by Django 5.0.3 on 2024-06-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0026_alter_stock_stock_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="stock_name",
            field=models.CharField(default="Oh my Gas", max_length=255),
        ),
    ]
