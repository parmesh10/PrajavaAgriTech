from django.contrib import admin
from .models import Product, ProductEnquiry


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "available",
        "featured",
        "created_at",
    )

    list_filter = (
        "category",
        "available",
        "featured",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "available",
        "featured",
    )

    ordering = (
        "-created_at",
    )

@admin.register(ProductEnquiry)
class ProductEnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "email",
        "product",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "product__name",
        "message",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )
    