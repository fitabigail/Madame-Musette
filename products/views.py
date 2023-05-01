from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# All products view.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    page_num = request.GET.get('page', 1)
    paginator = Paginator(products, 16)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
                'products': page_obj,
            }

    return render(request, 'products/products.html', context)

# Product details view


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

    