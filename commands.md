# custom Django management commands

### **Step-by-Step Guide**

1. **Create the Folder Structure**
   Inside one of your apps (e.g., `myapp`), create the following directory structure:

   ```
   myapp/
       management/
           __init__.py
           commands/
               __init__.py
               my_custom_command.py
   ```

2. **Write the Custom Command**
   In the `my_custom_command.py` file, define your custom command by subclassing `BaseCommand`.

   ```python
   # myapp/management/commands/my_custom_command.py

   from django.core.management.base import BaseCommand

   class Command(BaseCommand):
       help = 'Sorts products by descending ID and updates the "order" field sequentially using bulk update'

       def add_arguments(self, parser):
           parser.add_argument(
               'sort_field',
               type=str,
               help='Field to sort products by, e.g., "-id" or "title"'
           )

       def handle(self, *args, **kwargs):
           sort_field = kwargs['sort_field']  
           products = Product.objects.order_by(sort_field) 
          
          
           for index, product in enumerate(products, start=1):
               product.order = index  # Set the order field
          
           Product.objects.bulk_update(products, ['order'])
          
           self.stdout.write(f"Updated order for {products.count()} products")
           
   ```

3. **Run the Command**
   Once you've written your custom command, you can run it using:

   ```bash
   python manage.py my_custom_command "-id"
   ```
---

### **Detailed Breakdown**

- **Command Class**: The custom command is defined in a class called `Command`, which inherits from `BaseCommand`. You must implement the `handle()` method, which is where the main logic goes.
  
- **`help` Attribute**: This attribute gives a brief description of what the command does. It appears when running `python manage.py help <command>`.

- **`add_arguments` Method**: If your command needs arguments, you can define them in this method using Django’s argument parser. For example, the `name` argument allows you to pass a value when running the command.

- **`handle()` Method**: This method contains the core functionality of your command. It receives any arguments passed from the command line and processes them.

---

### **Key Points to Teach**

1. **Folder Structure**: Ensure they place their custom commands in the right folder structure inside `management/commands`.
   
2. **`add_arguments` Method**: Useful for passing dynamic arguments to the command.

3. **`BaseCommand` Methods**: Besides `handle()`, there are other methods like `self.stdout.write()` for printing output, and `self.stderr.write()` for errors.

4. **Command Testing**: They can unit test their commands by calling the command directly from their code using Django's `call_command()` function.

---
