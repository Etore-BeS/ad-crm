from django.core.management.base import BaseCommand
from myapp.models import Product, Purchase, Buyer, Producer  # import your models here
import requests
import json

class Command(BaseCommand):
    help = 'Updates the database with data from the API'

    def handle(self, *args, **options):
        url = "https://sandbox.hotmart.com/payments/api/v1/sales/history"
        headers = {
            'Content': 'application/json',
            'Authorization': 'Bearer YOUR_BEARER_TOKEN'
        }
        payload = {}

        next_page_token = None

        while True:
            if next_page_token:
                payload['page_token'] = next_page_token

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code == 200:
                data = response.json()

                for item in data:
                    product, _ = Product.objects.get_or_create(id=item['product']['id'], defaults={'name': item['product']['name']})
                    buyer, _ = Buyer.objects.get_or_create(name=item['buyer']['name'], defaults={'ucode': item['buyer']['ucode'], 'email': item['buyer']['email']})
                    producer, _ = Producer.objects.get_or_create(name=item['producer']['name'], defaults={'ucode': item['producer']['ucode']})

                    purchase, _ = Purchase.objects.update_or_create(
                        transaction=item['purchase']['transaction'],
                        defaults={
                            'product': product,
                            'buyer': buyer,
                            'producer': producer,
                            'is_subscription': item['purchase']['is_subscription'],
                            'warranty_expire_date': item['purchase']['warranty_expire_date'],
                            'approved_date': item['purchase']['approved_date'],
                            'tracking_source': item['purchase']['tracking']['source'],
                            'tracking_source_sck': item['purchase']['tracking']['source_sck'],
                            'tracking_external_code': item['purchase']['tracking']['external_code'],
                            'recurrency_number': item['purchase']['recurrency_number'],
                            'offer_code': item['purchase']['offer']['code'],
                            'payment_mode': item['purchase']['offer']['payment_mode'],
                            'order_date': item['purchase']['order_date'],
                            'price_value': item['purchase']['price']['value'],
                            'currency_code': item['purchase']['price']['currency_code'],
                            'payment_method': item['purchase']['payment']['method'],
                            'installments_number': item['purchase']['payment']['installments_number'],
                            'payment_type': item['purchase']['payment']['type'],
                            'commission_as': item['purchase']['commission_as'],
                            'hotmart_fee_percentage': item['purchase']['hotmart_fee']['percentage'],
                            'hotmart_fee_base': item['purchase']['hotmart_fee']['base'],
                            'hotmart_fee_total': item['purchase']['hotmart_fee']['total'],
                            'hotmart_fee_fixed': item['purchase']['hotmart_fee']['fixed'],
                            'status': item['purchase']['status']
                        }
                    )

                if 'next_page_token' in data['page_info']:
                    next_page_token = data['page_info']['next_page_token']
                else:
                    break
            else:
                self.stdout.write(self.style.ERROR(f'Request failed with status code {response.status_code}'))
                break

        self.stdout.write(self.style.SUCCESS('Database update complete'))