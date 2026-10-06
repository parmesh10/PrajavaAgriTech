from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:pk>/enquiry/", views.product_enquiry, name="product_enquiry"),
    path("enquiry/success/", views.enquiry_success, name="enquiry_success"),
]