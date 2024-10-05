# scheduling tasks with Celery

### **1. Install `celery[redis]` and `django-celery-beat`**

To schedule tasks, we’ll use the **`django-celery-beat`** package, which stores periodic tasks in the Django database:

```bash
pip install celery[redis] django-celery-beat
```

### **2. Configure `django-celery-beat` in `settings.py`**

In your `settings.py`, make sure you add `django_celery_beat` to your `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # other apps
    'django_celery_beat',
]
```

Also, configure your Celery settings if not done already:

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```

### **3. Apply Migrations**

Run migrations to create the necessary database tables for `django-celery-beat`:

```bash
python manage.py migrate django_celery_beat
```

### **4. Create a Task to Schedule**

Let’s assume you want to update product prices regularly. You can create a task like this in `tasks.py` (inside your `product` app):

```python
# product/tasks.py

from celery import shared_task
from .models import Product

@shared_task
def update_all_product_prices():
    products = Product.objects.all()
    for product in products:
        product.price += 10  # Increment price by 10 (example)
        product.save()
    return "Product prices updated"
```

This task updates the price of all products.

### **5. Scheduling Tasks with `django-celery-beat`**

To schedule tasks, you’ll use the Django Admin to set up periodic tasks. First, make sure you have the **Django Admin** enabled.

In `admin.py`, register the periodic task models:

```python
# myproject/admin.py

from django.contrib import admin
from django_celery_beat.models import PeriodicTask, IntervalSchedule

admin.site.register(PeriodicTask)
admin.site.register(IntervalSchedule)
```

Then, start your Django server:

```bash
python manage.py runserver
```

Go to the Django Admin (`/admin`), and you’ll now see options for **Interval Schedules** and **Periodic Tasks**.

1. **Create an Interval** (e.g., every 10 minutes):
   - Go to **Interval Schedules** in the admin.
   - Create a new schedule (e.g., every 10 minutes).

2. **Create a Periodic Task**:
   - Go to **Periodic Tasks** in the admin.
   - Add a new task:
     - **Name**: `Update Product Prices`
     - **Task (import path)**: `product.tasks.update_all_product_prices`
     - **Interval**: Select the interval you just created (e.g., every 10 minutes).

### **6. Running the Scheduler**

To start the periodic task scheduler, you need to run the Celery **beat** service along with your worker:

```bash
celery -A myproject beat --loglevel=INFO
```

Also, run the Celery worker in another terminal:

```bash
celery -A myproject worker --loglevel=INFO
```

Now, the `update_all_product_prices` task will run based on the schedule you configured (e.g., every 10 minutes).

---

### **Example Recap:**

1. Install `django-celery-beat` and add it to your `INSTALLED_APPS`.
2. Apply migrations for `django-celery-beat`.
3. Define a Celery task (like updating all product prices).
4. Use the Django Admin to schedule periodic tasks.
5. Run the Celery **beat** and **worker** services to handle scheduled tasks.

This way, you can schedule any task using Celery and `django-celery-beat` in Django!
