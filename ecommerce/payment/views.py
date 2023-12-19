from django.shortcuts import render

from .models import ShippingAddress

# Create your views here.

def checkout(request):
    # logged in user
    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            return render(request, 'payment/checkout.html', {
                'shipping': shipping_address,
                })
        except ShippingAddress.DoesNotExist:
            return render(request, 'payment/checkout.html')
    else:
        # guest user
        return render(request, 'payment/checkout.html')


def payment_success(request):
    return render(request, 'payment/payment_success.html')


def payment_failed(request):
    return render(request, 'payment/payment_failed.html')