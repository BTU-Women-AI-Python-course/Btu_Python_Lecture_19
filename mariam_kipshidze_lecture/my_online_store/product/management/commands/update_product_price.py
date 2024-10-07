from django.core.management.base import BaseCommand

from product.models import Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        for product in products:
            product.price = product.price * 2
            product.save(update_fields=['price'])

        self.stdout.write(f"Updated price for {products.count()} products")
