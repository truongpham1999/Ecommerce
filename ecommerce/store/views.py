from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404

def store(request):
    all_products = Product.objects.all()
    return render(request, 'store/store.html', {
        'all_products': all_products,
    })

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def list_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list_category.html', {
        'products': products,
        'category': category,
    })

def product_infor(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_infor.html', {
        'product': product,
    }) 