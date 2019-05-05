from django.db import models

# Create your models here.
class Kidszone(models.Model):
        title = models.CharField(max_length=30)
        location = models.CharField(max_length=100)
        description = models.TextField()
        image = models.FileField(blank=True)
        password = models.CharField(max_length=50)
        
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)

class Board(models.Model):
        nick = models.CharField(max_length=30)
        title = models.CharField(max_length=30)
        description = models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        password = models.CharField(max_length=50)
        
        # 0 : 자유게시판, 1: 공지사항,  2: QnA, 
class Boards(models.Model):
        
        title = models.CharField(max_length=30)
        description = models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        password = models.CharField(max_length=50)
        
class Review(models.Model):
        title = models.CharField(max_length=30)
        writer = models.CharField(max_length=100)
        your_review = models.TextField()
        image = models.FileField()
        password = models.CharField(max_length=50)
        kidszoneID = models.IntegerField(blank=True, default=0)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        
