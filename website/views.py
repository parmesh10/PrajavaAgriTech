from django.shortcuts import render
from products.models import Product


def home(request):
    featured_products = Product.objects.filter(
        available=True,
        featured=True
    )[:6]

    return render(
        request,
        "website/home.html",
        {
            "featured_products": featured_products
        }
    )