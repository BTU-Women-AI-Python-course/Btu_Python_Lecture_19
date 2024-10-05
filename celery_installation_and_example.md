# Setting up Celery

### **1. Install Celery**

First, install Celery and a broker like Redis:

```bash
pip install celery redis
```

### **2. Configure Django Settings for Celery**

In your `settings.py`, add the basic Celery configuration:

```python
# settings.py

CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Use Redis as broker
CELERY_ACCEPT_CONTENT = ['json']  # Accept JSON
CELERY_TASK_SERIALIZER = 'json'  # Serialize tasks as JSON
```

### **3. Create Celery Configuration**

In your Django project directory (next to `settings.py`), create a file called `celery.py`:

```python
# myproject/celery.py

import os
from celery import Celery

# Set default Django settings for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Create Celery app
app = Celery('myproject')

# Load configuration from settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks automatically from your apps
app.autodiscover_tasks()
```

In your `__init__.py` (same directory as `celery.py`), add:

```python
# myproject/__init__.py

from .celery import app as celery_app

__all__ = ['celery_app']
```

### **4. Define a Task Using the Product Model**

In your app (e.g., `product`), create a file `tasks.py` where you define your Celery tasks.

Here’s an example using your **Product** model:

```python
# product/tasks.py

from celery import shared_task
from .models import Product

@shared_task
def update_product_price(product_id, new_price):
    try:
        product = Product.objects.get(id=product_id)
        product.price = new_price
        product.save()
        return f"Product {product.name} price updated to {new_price}"
    except Product.DoesNotExist:
        return f"Product with id {product_id} does not exist"
```

This task updates the price of a product asynchronously.

### **5. Run Celery Worker**

To process tasks, start the Celery worker in your project directory:

```bash
celery -A myproject worker --loglevel=INFO
```

### **6. Call the Task**

You can call this task asynchronously from your views, like so:

```python
# views.py

from product.tasks import update_product_price

def change_price(request, product_id, new_price):
    update_product_price.delay(product_id, new_price)
    return HttpResponse(f'Updating price for Product {product_id}')
```

Using `.delay()`, the task will be executed asynchronously in the background.

---

### Recap:
1. Install Celery and Redis.
2. Set up basic configuration in `settings.py`.
3. Create `celery.py` and configure it.
4. Define tasks in `tasks.py`.
5. Start the Celery worker to handle background tasks.

This setup will allow you to run tasks asynchronously using the **Product** model in your Django project.
