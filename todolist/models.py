from django.utils import timezone
from django.db import models 
class Category(models.Model):
   name=models.CharField( max_length=100)

# Create your models here.
class ToDoList(models.Model):
   title=models.CharField(max_length=250)
   content=models.TextField(blank=True)
   created=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
   due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
   # category = models.ForeignKey(Category, default="general")
   
   

   def __str__(self):
        return self.title 