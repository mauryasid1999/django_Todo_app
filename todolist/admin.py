from django.contrib import admin

# Register your models here.
from . import models
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(models.ToDoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)