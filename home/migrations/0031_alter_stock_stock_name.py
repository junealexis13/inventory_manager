# Generated by Django 5.0.6 on 2024-07-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_product_category_alter_stock_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(default='Oh my Gas', max_length=255),
        ),
    ]
