# Generated by Django 5.0.6 on 2024-06-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_product_cost_price_product_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
