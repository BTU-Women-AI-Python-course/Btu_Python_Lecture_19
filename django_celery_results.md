# Django celery results

### 1. **Install `django-celery-results`**

First, install the `django-celery-results` package:

```bash
pip install django-celery-results
```

### 2. **Add `django_celery_results` to `INSTALLED_APPS`**

In your Django project's `settings.py`, add `django_celery_results` to the `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    'django_celery_results',
]
```

### 3. **Configure Celery Results Backend**

Set the results backend to use Django's database by adding this to `settings.py`:

```python
CELERY_RESULT_BACKEND = 'django-db'
```

If you want to store results in the cache as well, you can use:

```python
CELERY_CACHE_BACKEND = 'django-cache'
```

### 4. **Run Migrations**

Run the migrations to create the necessary database tables to store Celery task results:

```bash
python manage.py migrate django_celery_results
```

### 5. **Using Celery Results**

Once `django-celery-results` is set up, Celery will automatically store the results of your tasks in the database.

You can access the result of a task using the task’s ID:

```python
from celery.result import AsyncResult

# Replace 'task_id' with the actual ID of a task
result = AsyncResult(task_id)

# Check the status of the task
print(result.status)

# Get the result (if the task has completed)
if result.status == 'SUCCESS':
    print(result.result)
```
