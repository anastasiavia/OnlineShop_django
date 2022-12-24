from django.db import models
from django.conf import settings
# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=12)

    def __str__(self):
        return self.item_name


class User(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    time_order = models.DateTimeField()


