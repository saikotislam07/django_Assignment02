from django.contrib import admin
from Task.models import TaskStoreModel
# Register your models here.

class TaskManagment(admin.ModelAdmin):
    list_display = ('Title', 'Description', 'Status')


    
admin.site.register(TaskStoreModel, TaskManagment)
