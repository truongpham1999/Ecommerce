from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress

        fields = ['full_name', 'phone_number', 'email', 'address1', 'address2', 'city', 'district', 'ward']

        exclude = ['user',]