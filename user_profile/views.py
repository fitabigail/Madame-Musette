from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Order

from .models import UserProfile
from .forms import UserProfileForm

# USER PROFILE (Copied fromBoutiqueAdo and adapted for MadameMusette


@login_required
def user_profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    purchases = profile.purchases.all()

    template = 'users_profiles/profile.html'

    context = {
        'form': form,
        'purchases': purchases,
        'on_profile_page': True
    }

    return render(request, template, context)


# ORDER HISTORY VIEW

def order_history(request, order_number):
    purchases = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'orders/order_complete.html'
    context = {
        'order': purchases,
        'from_profile': True,
    }

    return render(request, template, context)
