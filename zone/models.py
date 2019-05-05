from django.db import models

# Create your models here.
class Kidszone(models.Model):
        title = models.CharField(max_length=30)
        location = models.CharField(max_length=100)
        description = models.TextField()
        image = models.FileField()
        
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)

class Board(models.Model):
        title = models.CharField(max_length=30)
        description = models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)

