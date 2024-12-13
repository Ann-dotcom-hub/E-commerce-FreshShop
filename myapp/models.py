from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Image = models.ImageField(upload_to="media/products/")


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

