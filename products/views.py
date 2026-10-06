from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductEnquiryForm


def product_list(request):
    products = Product.objects.filter(available=True)

    category = request.GET.get("category")

    if category:
        products = products.filter(category=category)

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
            "categories": Product.CATEGORY_CHOICES,
        }
    )


def product_detail(request, pk):
    product = get_object_or_404(
        Product,
        pk=pk,
        available=True
    )

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product
        }
    )
def product_enquiry(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
        available=True
    )

    if request.method == "POST":

        form = ProductEnquiryForm(
            request.POST
        )

        if form.is_valid():

            enquiry = form.save(
                commit=False
            )

            enquiry.product = product

            enquiry.save()

            return redirect(
                "enquiry_success"
            )

    else:

        form = ProductEnquiryForm()

    return render(
        request,
        "products/product_enquiry.html",
        {
            "product": product,
            "form": form,
        }
    )


def enquiry_success(request):

    return render(
        request,
        "products/enquiry_success.html"
    )    