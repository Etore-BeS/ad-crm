# Generated by Django 5.0.4 on 2024-04-19 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_buyer_producer_product_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='adress',
            new_name='address',
        ),
    ]
