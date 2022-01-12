from django.db import models

# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50,default="inayat")
    address = models.CharField(max_length=150,default="delhi")
    phone = models.IntegerField(default='8171415434')
    date = models.DateField(auto_now_add=True)

class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class producat(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
