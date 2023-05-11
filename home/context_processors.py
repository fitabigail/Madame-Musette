from django.conf import settings
from .form import ContactForm


def contact_form(request):
    c_form = ContactForm()
    context = {
        'c_form': c_form,
    }
    return context
