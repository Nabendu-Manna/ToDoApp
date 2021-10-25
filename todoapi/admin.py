from django.contrib import admin

from django.contrib import admin
from todoapi.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'competed')

