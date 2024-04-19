from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)