# Generated by Django 5.0.4 on 2024-04-19 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ucode', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ucode', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('is_subscription', models.BooleanField()),
                ('warranty_expire_date', models.BigIntegerField()),
                ('approved_date', models.BigIntegerField()),
                ('tracking_source', models.CharField(max_length=255)),
                ('tracking_source_sck', models.CharField(max_length=255)),
                ('tracking_external_code', models.CharField(max_length=255)),
                ('recurrency_number', models.IntegerField()),
                ('transaction', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('offer_code', models.CharField(max_length=255)),
                ('payment_mode', models.CharField(max_length=255)),
                ('order_date', models.BigIntegerField()),
                ('price_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency_code', models.CharField(max_length=255)),
                ('payment_method', models.CharField(max_length=255)),
                ('installments_number', models.IntegerField()),
                ('payment_type', models.CharField(max_length=255)),
                ('commission_as', models.CharField(max_length=255)),
                ('hotmart_fee_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotmart_fee_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotmart_fee_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotmart_fee_fixed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotmart_fee_currency_code', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.buyer')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.producer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
        ),
    ]
