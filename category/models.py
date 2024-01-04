from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    CaategoryName = models.CharField(max_length=30)
    

    def __str__(self):
        return self.CaategoryName
