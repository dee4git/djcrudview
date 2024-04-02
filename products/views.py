from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .models import Product


# Create your views here.
def rate_product(request, p_id):
    product = Product.objects.get(pk=p_id)
    if request.method == "GET":
        form = forms.ProductRatingForm(request.GET)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.product = product
            instance.save()
            return HttpResponse('rate successful')
    else:
        form = forms.ProductRatingForm()
    return render(request, 'forms.html', {
        "form": form,
    })


def add_product(request):
    if request.method == "GET":
        form = forms.ProductForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('add successful')
    else:
        form = forms.ProductForm()
    return render(request, 'forms.html', {
        "form": form,
    })


def update_product(request, p_id):
    p = Product.objects.get(pk=p_id)
    if request.method == "GET":
        form = forms.ProductForm(request.GET or None, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponse('update successful')
    else:
        form = forms.ProductForm(instance=p)
    return render(request, 'forms.html', {
        "form": form,
    })


def delete_product(request, p_id):
    Product.objects.get(pk=p_id).delete()
    return HttpResponse('Delete successful')
