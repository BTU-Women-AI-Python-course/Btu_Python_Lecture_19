## Celery and Django Integration

This section provides an overview of integrating Celery with Django to handle asynchronous tasks efficiently:

- **Commands** - https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/
- **Celery - Setting up Django Settings and Defining Tasks** - https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html:
  - Configure your Django settings for Celery integration and define tasks to be executed asynchronously.
- **Running Tasks with Django**:
  - Learn how to run Celery tasks in a Django application, allowing for background processing of tasks.
- **Scheduling Tasks** - https://django-celery-beat.readthedocs.io/en/latest/:
  -  Use Celery to schedule tasks at specified intervals, enabling periodic execution of tasks for maintenance, data updates, and more.

## 📚 Task: Integrate Celery with Django for Asynchronous Email Sending

### 1. Install Celery and Set Up Django Settings:
- Install `celery` and `redis` as the message broker.
- Configure Celery in Django's settings and create a task to send an email asynchronously.

### 2. Define an Asynchronous Task:
- Create a task to send a email when a user registers (Welcome to our platform).
- The email should be sent asynchronously using Celery.

### 3. Schedule a Periodic Task:
- Set up Celery Beat to schedule a task that sends a randomly generated weekly newsletter.
