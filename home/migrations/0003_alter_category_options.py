# Generated by Django 5.0.3 on 2024-05-30 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_category_remove_product_dimensions_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
