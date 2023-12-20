from django.shortcuts import render

from .models import ShippingAddress, Order, OrderItem

from cart.cart import Cart

from django.http import JsonResponse

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
    

def complete_checkout(request):
    if request.POST.get('action') == 'post':
        # Get the form data
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        district = request.POST.get('district')
        ward = request.POST.get('ward')

        shipping_address = (address1 + "\n" + address2 + "\n" + city + "\n" + district + "\n" + ward)

        # cart information
        cart = Cart(request)
        total = cart.get_total_price()

        # create order
        if request.user.is_authenticated:
            order = Order.objects.create(
                user = request.user,
                full_name = name,
                phone_number = phone_number,
                email = email,
                shipping_address = shipping_address,
                amount_paid = total,
            )
            
            for item in cart:
                OrderItem.objects.create(
                    user = request.user,
                    order = order,
                    product = item['product'],
                    quantity = item['quantity'],
                    price = item['price'],
                )
        else:
            order = Order.objects.create(
                full_name = name,
                phone_number = phone_number,
                email = email,
                shipping_address = shipping_address,
                amount_paid = total,
            )

            for item in cart:
                OrderItem.objects.create(
                    order = order,
                    product = item['product'],
                    quantity = item['quantity'],
                    price = item['price'],
                )

        order_success = True
        return JsonResponse({'success': order_success})



def payment_success(request):
    # clear cart session
    del request.session['session_key']

    return render(request, 'payment/payment_success.html')


def payment_failed(request):
    return render(request, 'payment/payment_failed.html')