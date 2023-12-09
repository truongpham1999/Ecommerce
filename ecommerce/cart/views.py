from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .cart import Cart

from store.models import Product
from django.shortcuts import get_list_or_404

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart_summary.html', {
        'cart': cart,
    })


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity=product_quantity)
        cart_quantity = cart.__len__()

        response = JsonResponse({'product_quantity' : cart_quantity})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        cart_quantity = cart.__len__()
        total_price = cart.get_total_price()

        response = JsonResponse({
            'product_quantity': cart_quantity,
            'total_price': total_price,
        })
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('quantity'))
        cart.update(product_id=product_id, quantity=product_quantity)
        cart_quantity = cart.__len__()
        total_price = cart.get_total_price()

        response = JsonResponse({
            'product_quantity': cart_quantity,
            'total_price': total_price,
        })
        return response