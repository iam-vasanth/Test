from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Task


# Admin registration code for Task model.
class TaskAdmin(ModelAdmin):
    list_display = ("user", "created_at", "task")

admin.site.register(Task, TaskAdmin)