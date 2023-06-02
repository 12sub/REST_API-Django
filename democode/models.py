from django.db import models

# Create your models here.
class Works(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    information = models.CharField(max_length=150)
    description = models.TextField(default=None)
    date_of_birth = models.DateField(auto_now_add=True)