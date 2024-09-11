# Generated by Django 5.0.3 on 2024-09-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0005_alter_sellitem_date_transaction_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sellitem",
            name="total_margin",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
