from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def order(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart added")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'orders/orders.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)