from django import forms
from .models import ProductEnquiry


class ProductEnquiryForm(forms.ModelForm):

    class Meta:
        model = ProductEnquiry

        fields = [
            "name",
            "phone",
            "email",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your name"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter mobile number"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter email address"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your enquiry",
                    "rows": 5
                }
            ),
        }