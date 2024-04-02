from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    description = models.CharField(max_length=1000, default='abc')

    def __str__(self):
        return self.name + str(self.price)


class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
