from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ("machinery", "Agricultural Machinery"),
        ("tractor", "Tractors & Implements"),
        ("sprayer", "Sprayers"),
        ("pump", "Agricultural Pumps"),
        ("harvesting", "Harvesting Equipment"),
        ("tools", "Agricultural Tools"),
        ("irrigation", "Irrigation Products"),
        ("other", "Other Agricultural Products"),
    ]

    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
class ProductEnquiry(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="enquiries"
    )

    name = models.CharField(max_length=150)

    phone = models.CharField(max_length=20)

    email = models.EmailField(
        blank=True,
        null=True
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ("new", "New"),
            ("contacted", "Contacted"),
            ("completed", "Completed"),
        ],
        default="new"
    )

    def __str__(self):
        return f"{self.name} - {self.product.name}"

    class Meta:
        ordering = ["-created_at"]
        