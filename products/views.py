from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# All products view.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()    
    categories = None    
    sort = None
    direction = None       
        
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories, in_stock=True, is_customized=True,)
            categories = Category.objects.filter(name__in=categories)    

    page_num = request.GET.get('page', 1)
    paginator = Paginator(products, 16)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:        
        page_obj = paginator.page(1)
    except EmptyPage:       
        page_obj = paginator.page(paginator.num_pages)

    sorting_products = f'{sort}_{direction}'

    context = {
        'products': page_obj,
        'categories': categories,
        'sorting_products': sorting_products,              
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

# Search View


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            query = Q(name__icontains=keyword) | Q(description__icontains=keyword)
            products = Product.objects.order_by('-updated_date').filter(query)
            product_count = products.count()          
    
    data = {
        'keyword': keyword,
        'products': products,
        'product_count': product_count,       
    }
    return render(request, 'products/products.html', data)      