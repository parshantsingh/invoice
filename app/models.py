from django.db import models
import datetime

# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50,default="Vikas Sharma")
    address = models.CharField(max_length=150,default="IFCO Chowk, Delhi")
    phone = models.IntegerField(default='+91 8171415434')
    date = models.DateField(default=datetime.datetime.today)

class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)

class producat(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
