from django.db import models
from category.models import CategoryModel
# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    TaskAssignDate = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(CategoryModel)
    def __str__(self) :
        return self.taskTitle