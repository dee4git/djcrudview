from django.contrib import admin

# Register your models here.
from .models import Product, ProductRating

admin.site.register(Product)
admin.site.register(ProductRating)
