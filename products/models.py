from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)   
    name = models.CharField(max_length=254)
    description = RichTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True) 
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)   
    is_customized = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name