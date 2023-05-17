from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contactView, name='contactView'),
    path('about/', views.about, name='about'),
]
