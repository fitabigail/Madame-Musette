from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from formtools.preview import FormPreview
from .models import Product, Category, Customise, Review
from .forms import ProductForm, CustomiseForm, ReviewForm
from django.db.models.functions import Lower
from datetime import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


AUTO_ID = 'formtools_%s'

# ALL PRODUCTS VIEW.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    categories = None
    sort = None
    direction = None
    logged_user = request.user

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
            products = products.filter(category__name__in=categories,
                                       in_stock=True)
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
        'logged_user': logged_user,
       
    }
    return render(request, 'products/products.html', context)


# PRODUCT DETAILS VIEW


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    num_review = Review.objects.filter(product=product).count()
    context = {
        'product': product,
        'num_review': num_review,
    }

    return render(request, 'products/product_detail.html', context)

# REVIEW PRODUCT VIEW


def add_review(request, pk):
    product = Product.objects.get(id=pk)
    form = ReviewForm(instance=product)   

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=product)
       
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['body']
            review = Review(product=product, author=name, body=body, date_created=datetime.now())
            product_id = review.product.id            
            review.save()
            messages.success(request, 'Your review was submited')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'form is invalid') 
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }

    return render(request, 'products/add_review.html', context)       

# DELETE REVIEW VIEW


def delete_review(request, pk):
    review = Review.objects.filter(product=pk).last()
    product_id = review.product.id
    review.delete()
    return redirect(reverse('product_detail', args=[product_id]))


# PRODUCT CUSTOMISE VIEW


class CustomiseFormPreview(FormPreview):
    form_template = 'products/customise.html'
    preview_template = 'products/preview.html'

    def done(self, request, cleaned_data):
        Customise.objects.create(**cleaned_data)
        messages.success(request, 'Your Request was succesfuly registred, and \
                on short time we will contact you by email.')
        return redirect(reverse('home'))


# ADD PRODUCT VIEW (Product manager function copied from BoutiqueAdo)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please\
                 ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

# EDIT PRODUCT VIEW


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure \
                                     the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

# DELETE PRODUCT VIEW

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

#  SEARCH VIEW


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

# LIKE PRODUCT VIEW


def like_product(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    if product.like.filter(id=request.user.id).exists():
        product.like.remove(request.user)
    else:
        product.like.add(request.user)
    return redirect(reverse('product_detail', args=[product_id]))
