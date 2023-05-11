from django.shortcuts import render
from .models import Contact
from .form import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.


def index(request):
    """ A view to return the index page """
   
    return render(request, 'home/index.html')


def contactView(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was send succesfuly, soon one of our team member will contact you!')
            return HttpResponseRedirect('/')
        #else:            
            #print('INVALID: ', form.errors)    
        