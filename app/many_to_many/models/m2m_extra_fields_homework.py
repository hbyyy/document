from django.db import models


class Customer(models.Model):
    email = models.EmailField(max_length=20)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


class Shop(models.Model):
    name = models.CharField(max_length=20)
    customers = models.ManyToManyField(Customer, through='Shipping')


class Item(models.Model):
    name = models.CharField(max_length=20)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
