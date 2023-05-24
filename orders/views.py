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
        'stripe_public_key': 'pk_test_51NAvnoLMDDkkprFVsr1WMPmANlPdR4SAhC5OLY0saHSziZAlSY3MMKDg6BVPrmFCQsrrxfALh8CrNzltROSS1wFU00gsEgcoZ6',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)