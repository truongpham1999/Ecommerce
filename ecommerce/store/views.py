from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate_posts(posts, page_number, posts_per_page):
    # Pagination, show 10 products per page
    paginator = Paginator(posts, posts_per_page)

    # Get the current page number from the request's GET parameter
    page = page_number

    try:
        # Get the Page object for the requested page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        posts = paginator.page(paginator.num.pages)

    # Calculate previous and next page numbers
    previous_page = posts.previous_page_number() if posts.has_previous() else None
    next_page = posts.next_page_number() if posts.has_next() else None

    return posts, previous_page, next_page


def store(request):
    all_products = Product.objects.all()

    # Pagination, show 10 products per page
    products, previous_page, next_page = paginate_posts(all_products, request.GET.get('page'), 10)

    return render(request, 'store/store.html', {
        'products': products,
        'previous_page': previous_page,
        'next_page': next_page,
    })

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def list_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    products, previous_page, next_page = paginate_posts(products, request.GET.get('page'), 10)

    return render(request, 'store/list_category.html', {
        'products': products,
        'previous_page': previous_page,
        'next_page': next_page,
        'category': category,
    })

def product_infor(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_infor.html', {
        'product': product,
    }) 
