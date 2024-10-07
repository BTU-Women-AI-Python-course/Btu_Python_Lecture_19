from celery import shared_task
from product.models import Product

@shared_task
def update_product_price(product_id, new_price):
    try:
        product = Product.objects.get(id=product_id)
        product.price = new_price
        product.save(update_fields=['price'])
        return f"Product {product.title} price updated to {new_price}"
    except Product.DoesNotExist:
        return f"Product with id {product_id} does not exist"


@shared_task
def update_products_price():
    products = Product.objects.all()
    for product in products:
        product.price = 100
        product.save(update_fields=['price'])
    return f"Products price updated to 100"