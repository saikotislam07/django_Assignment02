from django.db import models

class TaskStoreModel(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Status = models.BooleanField(default=False)
    

