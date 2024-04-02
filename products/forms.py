from django import forms
from .models import Product, ProductRating


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
        ]


class ProductRatingForm(forms.ModelForm):
    class Meta:
        model = ProductRating
        fields = [
            'rating',
        ]
