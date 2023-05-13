from django.shortcuts import render

# Cart  view here.


def cart_view(request):
    """ A view to return the cart page """
   
    return render(request, 'cart/cart.html')

