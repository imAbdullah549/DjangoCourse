from django.db import models

# Create your models here.
class Category(models.Model):
    category_name: models.CharField(max_length=100)
    category_details:models.CharField(max_length=200)

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    category_Id = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    price = models.IntegerField(null=False)

class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()