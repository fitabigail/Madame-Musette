from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Cart  view here.


def cart_view(request):
    """ A view to return the cart page """
    
    return render(request, 'cart/cart.html')

# Add to cart view copied from BoutiqueAdo


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    cart = request.session.get('cart', {})
    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart    
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart_view'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    #product = get_object_or_404(Product(), pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                # messages.success(request, f'{product.item_id}"removed from your cart')
        else:
            cart.pop(item_id)
            # messages.success(request, f'{product.item_id}"removed from your cart')   

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        # messages.error(
            # request, f'An error occured removing "{e}" from your cart')
        return HttpResponse(status=500)