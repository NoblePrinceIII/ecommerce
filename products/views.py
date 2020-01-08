from django.shortcuts import render

from .models import Product


def home(request):

    template = 'home.html'
    context = locals()
    return render(request, template, context)


def all_products(request):

    products = Product.objects.all()
    context = {'products': products}
    template = 'all.html'
    return render(request, template, context)
