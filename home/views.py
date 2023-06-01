from django.shortcuts import render
from .models import Contact, Designer
from .form import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Home page view here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

# Contact form view here


def contactView(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was send succesfuly, \
                        soon one of our team member will contact you!')
            return HttpResponseRedirect('/')

# About page view


def about(request):
    designers = Designer.objects.all()

    data = {
        'designers': designers,
    }
    return render(request, 'home/about.html', data)
